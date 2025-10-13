from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class ShippingAddress(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.address_title_id = "enterShippingAddressTV"
        self.full_name_field_id = "fullNameET"
        self.address_one_field_id = "address1ET"
        self.address_two_field_id = "address2ET"
        self.city_field_id = "cityET"
        self.state_field_id = "stateET"
        self.zip_code_field_id = "zipET"
        self.country_field_id = "countryET"
        self.payment_btn_id = "paymentBtn"
        self.error_empty_name_id = "fullNameErrorTV"
        self.error_empty_address_one_id = "address1ErrorTV"
        self.error_empty_city_id = "cityErrorTV"
        self.error_empty_zip_code_id = "zipErrorTV"
        self.error_empty_country_id = "countryErrorTV"

    def go_to_payment(self):
        self.click_element(AppiumBy.ID, self.payment_btn_id)
    
    def get_title(self):
        return self.get_element_text(AppiumBy.ID, self.address_title_id)
    
    def fill_forms_completely(self, load_data):
        self.send_keys_to_element(AppiumBy.ID, self.full_name_field_id, load_data["shipping_address"]["full_name"])
        self.send_keys_to_element(AppiumBy.ID, self.address_one_field_id, load_data["shipping_address"]["address_one"])
        self.send_keys_to_element(AppiumBy.ID, self.address_two_field_id, load_data["shipping_address"]["address_two"])
        self.send_keys_to_element(AppiumBy.ID, self.city_field_id, load_data["shipping_address"]["city"])
        self.send_keys_to_element(AppiumBy.ID, self.state_field_id, load_data["shipping_address"]["state"])
        self.send_keys_to_element(AppiumBy.ID, self.zip_code_field_id, load_data["shipping_address"]["zip_code"])
        self.send_keys_to_element(AppiumBy.ID, self.country_field_id, load_data["shipping_address"]["country"])
        
    def assert_is_all_errors_displayed(self):
        assert self.is_element_displayed(AppiumBy.ID, self.error_empty_name_id), f"Empty full name error did not appear on Shipping Address screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_empty_address_one_id), f"Empty address one error did not appear on Shipping Address screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_empty_city_id), f"Empty city error did not appear on Shipping Address screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_empty_zip_code_id), f"Empty zip code error did not appear on Shipping Address screen"
        assert self.is_element_displayed(AppiumBy.ID, self.error_empty_country_id), f"Empty country error did not appear on Shipping Address screen"