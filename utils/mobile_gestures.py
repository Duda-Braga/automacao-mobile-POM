# Arquivo: utils/mobile_gestures.py

from appium.webdriver.webdriver import WebDriver
# Se o seu driver for apenas WebDriver do Selenium (para Appium 2.x), 
# você pode apenas usar 'WebDriver' para tipagem.

class MobileGestures:
    """
    Classe para encapsular gestos e interações móveis complexas
    usando a API mobile: do Appium.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scroll_screen(self, direction: str, percent: float = 1.0):
        """
        Executa um gesto de scroll na tela na direção especificada.

        Args:
            direction (str): A direção do scroll ("up" ou "down").
            percent (float): A força/distância do scroll (padrão 1.0).
        """
        # Garante que a direção seja válida
        if direction.lower() not in ["up", "down"]:
            raise ValueError("A direção deve ser 'up' ou 'down'.")
            
        size = self.driver.get_window_size()
        screen_width = size['width']
        screen_height = size['height']

        # Define as coordenadas de scroll (um ponto centralizado)
        # Inicia o toque a 30% da altura, move 50% da altura da tela.
        self.driver.execute_script("mobile: scrollGesture", {
            "left": 0,
            "top": screen_height * 0.3, 
            "width": screen_width,
            "height": screen_height * 0.5, 
            "direction": direction.lower(), # Usa o parâmetro aqui
            "percent": percent
        })

    # Aqui você poderia adicionar outras funções como swipe_to_element, long_press, etc.




''''
Importar a classe MobileGestures.
Instanciá-la no método __init__ da sua Page Object.

chamadno no page

# IMPORTAR O UTILITÁRIO
from utils.mobile_gestures import MobileGestures 

class ShippingAddress(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # ... (Seus IDs) ...
        self.payment_btn_id = "paymentBtn"
        
        # INSTANCIAR O UTILITÁRIO
-->     self.gestures = MobileGestures(driver) 

    def go_to_payment(self):
        # Primeiro, Garante que o botão 'Payment' esteja visível
        # Se o botão estiver lá embaixo, faça o scroll antes de clicar
        
        # Tenta clicar. Se der erro de elemento invisível, faz o scroll.
        try:
             self.click_element(AppiumBy.ID, self.payment_btn_id)
        except Exception: 
             # Se o elemento não foi encontrado, rola para baixo
             self.gestures.scroll_screen(direction="down")
             self.click_element(AppiumBy.ID, self.payment_btn_id)
             
        time.sleep(1)

    # ... (Seu fill_forms_completely) ...

'''