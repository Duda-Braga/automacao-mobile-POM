import pytest
import json
import base64
from pathlib import Path
from appium import webdriver
from appium.options.common.base import AppiumOptions

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshot_name = f"error_screenshot/screenshot_{item.name}.png"
            driver.get_screenshot_as_file(screenshot_name)
            print(f"Screenshot saved as {screenshot_name}")

@pytest.fixture(scope="function")
def driver(request):
    # --- SETUP PHASE ---
    options = AppiumOptions()
    options.load_capabilities({ 
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appWaitActivity": "com.saucelabs.mydemoapp.android.view.activities.MainActivity",
        "appWaitDuration": 30000, # opcional, tempo de espera em ms (30s)
        "uiautomator2ServerLaunchTimeout": 30000,
        "uiautomator2ServerInstallTimeout": 30000,
        "unicodeKeyboard": False,
        "resetKeyboard": True,
        
        #capabilities paara gravar screenshot
        "appium:androidScreenshotOnFai": True, # A redundant but good practice capability
        "appium:nativeWebScreenshot": True,
        "appium:recordVideo": "true", # Enable video recording
        "appium:videoType": "mpeg4"  # Specify video format

     }) # Capabilities defined here
    
    try:
        _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        _driver.start_recording_screen() # Start recording
    except Exception as e:
        pytest.skip(f"Failed to create Appium driver: {e}")

    
    # The 'yield' keyword passes control to the test function
    yield _driver
    

    # --- TEARDOWN PHASE ---
    # This code runs AFTER the test function completes (or fails)
    if _driver:
        # Stop recording and get the video data
        video_data = _driver.stop_recording_screen()

        # 2. VERIFICAÇÃO CONDICIONAL DE FALHA
        test_node = request.node
        # Verifica se o hook anexou o relatório 'rep_call' E se o teste falhou.
        is_failed = getattr(test_node, "rep_call", None) and test_node.rep_call.failed

        if is_failed and video_data:
            # Create a unique filename for the video
            video_filename = f"error_video/video_{request.node.name}.mp4"
            with open(video_filename, "wb") as f:
                f.write(base64.b64decode(video_data))
            print(f"Video saved as {video_filename}")
        _driver.quit()

@pytest.fixture(scope="session")
def load_data():
    """Lê o JSON de data e retorna como dicionário"""
    json_path = Path(__file__).parent / "data" / "test_data.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Este hook garante que o resultado do teste (sucesso, falha, skip)
    seja anexado ao objeto item (request.node) para uso posterior no teardown.
    """
    # 1. Executa todos os outros hooks para obter o objeto report
    outcome = yield
    rep = outcome.get_result()

    # 2. Anexa o objeto 'rep' (que tem o atributo 'failed') ao item do teste.
    # Usamos o stage 'call' pois é o que contém o resultado do assert
    if rep.when == "call":
        item.rep_call = rep