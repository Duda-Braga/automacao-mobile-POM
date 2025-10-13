from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from utils.mobile_gestures import MobileGestures 
import time 

class PaymentMethod(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.payment_title_id = "enterPaymentMethodTV"
        self.full_name_field_id = "nameET"
        self.card_number_field_id = "cardNumberET"
        self.expiration_date_field_id = "expirationDateET"
        self.security_code_field_id = "securityCodeET"
        self.review_order_btn_id = "paymentBtn"

        self.error_full_name_id = "nameErrorIV"
        self.error_card_number_id = "cardNumberErrorIV"
        self.error_expiration_date_id = "expirationDateIV"
        self.error_security_code_id = "securityCodeIV"

        self.billing_address_check_id = "billingAddressCB"

        self.full_name_address_field_id = "fullNameET"
        self.address_one_field_id = "address1ET"
        self.address_two_field_id = "address2ET"
        self.city_field_id = "cityET"
        self.state_field_id = "stateET"
        self.zip_code_field_id = "zipET"
        self.country_field_id = "countryET"

        self.error_name_address_id = "fullNameErrorIV"
        self.error_address_one_id = "address1ErrorIV"
        self.error_city_id = "cityIV"
        self.error_zip_code_id = "zipIV"
        self.error_country_id = "countryIV"

        self.gestures = MobileGestures(driver) 

    def get_title(self):
        return self.get_element_text(AppiumBy.ID, self.payment_title_id)

    def go_to_review_order(self):
        self.click_element(AppiumBy.ID, self.review_order_btn_id)
        time.sleep(1)

    def assert_is_all_card_errors_displayed(self):
        assert self.is_element_displayed(AppiumBy.ID, self.error_full_name_id), f"Full name error did not appear on Payment Screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_card_number_id), f"Card number error did not appear on Payment Screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_expiration_date_id), f"Expiration date error did not appear on Payment Screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_security_code_id), f"Security code error did not appear on Payment Screen"

    def fill_forms_card(self, load_data):
        self.send_keys_to_element(AppiumBy.ID, self.full_name_field_id, load_data["payment_method"]["full_name"])
        self.send_keys_to_element(AppiumBy.ID, self.card_number_field_id, load_data["payment_method"]["card_number"])
        self.send_keys_to_element(AppiumBy.ID, self.expiration_date_field_id, load_data["payment_method"]["expiration_date"])
        self.send_keys_to_element(AppiumBy.ID, self.security_code_field_id, load_data["payment_method"]["security_code"])
        
    def is_checked_same_billing_address(self):
        return self.is_element_checked(AppiumBy.ID, self.billing_address_check_id)
    
    def click_billing_address(self):
        self.click_element(AppiumBy.ID, self.billing_address_check_id)

    def fill_forms_billing_address(self, load_data):
        self.gestures.scroll_screen(direction="down")
        self.send_keys_to_element(AppiumBy.ID, self.full_name_address_field_id, load_data["billing_address"]["full_name"])
        self.send_keys_to_element(AppiumBy.ID, self.address_one_field_id, load_data["billing_address"]["address_one"])
        self.send_keys_to_element(AppiumBy.ID, self.address_two_field_id, load_data["billing_address"]["address_two"])
        self.send_keys_to_element(AppiumBy.ID, self.city_field_id, load_data["billing_address"]["city"])
        self.send_keys_to_element(AppiumBy.ID, self.state_field_id, load_data["billing_address"]["state"])
        self.send_keys_to_element(AppiumBy.ID, self.zip_code_field_id, load_data["billing_address"]["zip_code"])
        self.send_keys_to_element(AppiumBy.ID, self.country_field_id, load_data["billing_address"]["country"])

    def assert_is_all_billing_adddress_errors_displayed(self):
        self.gestures.scroll_screen(direction="down")
        assert self.is_element_displayed(AppiumBy.ID, self.error_name_address_id), f"Empty full name error did not appear on Payment Screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_address_one_id), f"Empty address one error did not appear on Payment Screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_city_id), f"Empty city error did not appear on Payment Screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_zip_code_id), f"Empty zip code error did not appear on Payment Screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_country_id), f"Empty country error did not appear on Payment Screen"
