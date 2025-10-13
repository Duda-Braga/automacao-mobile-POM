from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class Login(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.login_title_id = "loginTV"
        self.login_btn_id = "loginBtn"
        self.user_field_id = "nameET"
        self.password_field_id = "passwordET"
        self.error_empty_user_id = "nameErrorTV"
        self.error_empty_user_id = "nameErrorTV"
        self.error_empty_password_id = "passwordErrorTV"
        self.first_user_id = "username1TV"

    def get_login_title(self):
        return self.get_element_text(AppiumBy.ID, self.login_title_id)
    
    def do_login(self):
        self.click_element(AppiumBy.ID, self.login_btn_id)

    def is_username_error_display(self):
        self.is_element_displayed(AppiumBy.ID, self.error_empty_user_id)

    def is_password_error_display(self):
        self.is_element_displayed(AppiumBy.ID, self.error_empty_password_id)

    def get_error_user(self):
        self.get_element_text(AppiumBy.ID, self.error_empty_user_id)

    def get_error_password(self):
        self.get_element_text(AppiumBy.ID, self.error_empty_password_id)

    def do_first_login_example(self):
        self.click_element(AppiumBy.ID, self.first_user_id)

    def fill_user(self, user):
        self.send_keys_to_element(AppiumBy.ID, self.user_field_id, user)

    def fill_password(self, password):
        self.send_keys_to_element(AppiumBy.ID, self.password_field_id, password)
