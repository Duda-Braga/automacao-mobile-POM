from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from utils.mobile_gestures import MobileGestures 
import time 

class ReviewOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



    # Validate that the Checkout, Review your order screen has been displayed.
    # Validate that the Deliver Address and Payment Method information is correct
    # Validate the product's unit information such as Name and Value
    # Validate that the total value of the items plus the Freight value is correct.
    # Click on the Place Order button