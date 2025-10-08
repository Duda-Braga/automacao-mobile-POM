from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title_id = "productTV"
        self.orange_backpack_xpath = "//android.widget.TextView[@content-desc='Product Title' and @text='Sauce Labs Backpack (orange)']/../android.widget.ImageView"

    def get_home_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.product_title_id)

    def select_orange_backpack(self):
        self.click_element(AppiumBy.XPATH, self.orange_backpack_xpath)
        

