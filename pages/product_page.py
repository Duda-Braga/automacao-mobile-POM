from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
import time

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.backpack_name_id = "productTV"
        self.plus_btn_id = "plusIV"
        self.minus_btn_id = "minusIV"
        self.qtt_product_id = "noTV"
        self.add_cart_btn_id = "cartBt"
        self.cart_icon_id = "cartIV"
        self.cart_icon_qtt_id = "cartTV"
        self.product_uinty_value_id = "priceTV"

    
    def get_product_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.backpack_name_id)

    def get_product_quantity(self):
        return int(self.get_element_text(AppiumBy.ID, self.qtt_product_id))
    
    def get_product_unity_value(self):
        return float(self.get_element_text(AppiumBy.ID, self.product_uinty_value_id)[2:])

    def increase_qunatity(self):
        self.click_element(AppiumBy.ID, self.plus_btn_id)

    def decrease_qunatity(self):
        self.click_element(AppiumBy.ID, self.minus_btn_id)

    def decrease_quantity_untill_X(self, x):
        while self.get_product_quantity() > x:
            self.decrease_qunatity()
        
    def increase_quantity_untill_X(self, x):
        while self.get_product_quantity() < x:
            self.increase_qunatity()

    def add_to_cart(self):
        self.click_element(AppiumBy.ID, self.add_cart_btn_id)
    
    def get_cart_quantity(self):
        return int(self.get_element_text(AppiumBy.ID, self.cart_icon_qtt_id))

    def is_add_cart_clickable(self):
        return self.is_element_enabled(AppiumBy.ID, self.add_cart_btn_id)
    
    def go_to_cart(self):
        self.click_element(AppiumBy.ID, self.cart_icon_id)
        time.sleep(1)

