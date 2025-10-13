from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class MyCart(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.mycart_page_title_id = "productTV"
        self.mycart_name_product_id = "titleTV"
        self.mycart_unity_price_id = "priceTV"
        self.mycart_qtt_product_id = "noTV"
        self.mycart_total_qtt_id = "itemsTV"
        self.mycart_total_value_id = "totalPriceTV"
        self.mycart_proceed_checkout_btn_id = "cartBt"

    def get_mycart_title(self):
        return self.get_element_text(AppiumBy.ID, self.mycart_page_title_id)
    
    def get_product_name(self):
        return self.get_element_text(AppiumBy.ID, self.mycart_name_product_id)
    
    def get_unity_price_product(self):
        return float(self.get_element_text(AppiumBy.ID, self.mycart_unity_price_id)[2:])

    def get_unity_qtt(self):
        return int(self.get_element_text(AppiumBy.ID, self.mycart_qtt_product_id))
    
    def get_total_qtt(self):
        return int(self.get_element_text(AppiumBy.ID, self.mycart_total_qtt_id)[:1])
    
    def get_total_purchase_value(self):
        return float((self.get_element_text(AppiumBy.ID, self.mycart_total_value_id)[2:]))
    
    def go_to_proced_checkout(self):
        self.click_element(AppiumBy.ID, self.mycart_proceed_checkout_btn_id)
        