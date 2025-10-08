import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions

@pytest.fixture(scope="function")
def driver():
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
        "resetKeyboard": True
     }) # Capabilities defined here
    
    _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    # The 'yield' keyword passes control to the test function
    yield _driver
    
    # --- TEARDOWN PHASE ---
    # This code runs AFTER the test function completes (or fails)
    print("\nQuitting driver...")
    _driver.quit()