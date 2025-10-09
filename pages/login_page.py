from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
import time

class Login(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.login_title_id = "loginTV"
        self.login_btn_id = "loginBtn"
        self.user_field_id = "nameET"
        self.password_field_id = "passwordET"
        self.error_empty_user_id = "nameErrorTV"
        self.error_empty_password_id = ""


    def get_login_title(self):
        return self.get_element_text(AppiumBy.ID, self.login_title_id)
    
    def do_login(self):
        self.click_element(AppiumBy.ID, self.login_btn_id)




    # Validate that the Login screen has been displayed
    # Try to log in without entering Username and Password and validate the error in the Username field
    # Try to log in without entering Password and validate the error in the Password field
    # Capture the first Username from the Usernames list at the bottom of the screen and enter this value in the Username field
    # Capture the Password from the Password list at the bottom of the screen and enter this value in the Password field
    # Click on the Login button