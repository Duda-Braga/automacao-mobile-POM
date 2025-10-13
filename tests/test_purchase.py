import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.myCart_page import MyCart
from pages.login_page import Login
from pages.shippingAddress_page import ShippingAddress
from pages.payment_page import PaymentMethod

import time

# Import other page objects as needed
# Test test to purchase 1 type of item
def test_product_selection(driver,load_data):

    # Initialize page objects with the driver provided by the fixture
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    mycart_page = MyCart(driver)
    login_page = Login(driver)
    address_page = ShippingAddress(driver)
    payment_page = PaymentMethod(driver)

    # item of test
    expected_product_name = "Sauce Labs Backpack (orange)"
    expeected_product_quantity = 2
    expected_unity_value = product_page.get_product_unity_value()
    expeted_total_item_value = expected_unity_value * expeected_product_quantity

    #data 
    user = "Test user"


    # Perform actions using page object methods
    assert home_page.get_home_page_title() == "Products", f"It should be in Products screen, but it is in {home_page.get_home_page_title()}"
    home_page.select_orange_backpack()

    # Continue with product page interactions
    # validate the correct product page oppended

    ### PRODUCT PAGE
    assert product_page.get_product_page_title() == expected_product_name
    
    # Decrease qtt '-' and validate that the quantity has decreased by 1 unit
    inicial_value = product_page.get_product_quantity()
    product_page.decrease_qunatity()
    new_value = product_page.get_product_quantity()
    assert new_value ==  inicial_value-1, f"Quantity did not decrease, it should be {inicial_value - 1} but is {new_value}"

    # validate zero quantity of products the Add to cart button will become inactive.
    if new_value > 0:
        product_page.decrease_quantity_untill_X(0)
    assert not product_page.is_add_cart_clickable(), "Add to cart button should not work with zero itens"
    
    # increase the quantity for 2 units and check if the add to cart button is enable then click it
    product_page.increase_quantity_untill_X(expeected_product_quantity)
    final_value = product_page.get_product_quantity()
    assert final_value == new_value+expeected_product_quantity, f"It should increase {expeected_product_quantity} itens, it incresed {final_value-new_value}"
    product_page.add_to_cart()

    # Validate that a circle has appeared in the cart icon informing you of the exact number of items you have added to the cart
    assert product_page.get_cart_quantity() == final_value, f"Wrong qunatity in the cart it should be {final_value}"
    
    #open the cart
    product_page.go_to_cart()

    ### MY CART PAGE

    # Validate that the My Cart screen has been opened
    assert mycart_page.get_mycart_title() == "My Cart", f"It should be in My Cart screen, but it is in {mycart_page.get_mycart_title()}"

    # Validate that your product is correct
    assert mycart_page.get_product_name() == expected_product_name, f"{expected_product_name} should be in the cart, but it is {mycart_page.get_product_name()}"

    # Validate that the unit price is as expected
    assert mycart_page.get_unity_price_product() == expected_unity_value, f"The product price should be {expected_unity_value}, but it is {mycart_page.get_unity_price_product()}"

    # Validate that the quantity is correct in the field below the product photo
    assert mycart_page.get_unity_qtt() == expeected_product_quantity, f"Product quantity should be {expeected_product_quantity}, but it is {mycart_page.get_unity_qtt()}"

    # Validate that the quantity is correct in the Total: x Items field
    assert mycart_page.get_total_qtt() == expeected_product_quantity, f"Total product quantity should be {expeected_product_quantity}, but it is {mycart_page.get_total_qtt()}"
    
    # Validate that the total value of the purchase is as expected for 2 units of the product
    assert mycart_page.get_total_purchase_value() == expeted_total_item_value, "Total value in My Cart should be "
    
    # Click on the Proceed To Checkout button
    mycart_page.go_to_proced_checkout()

    ### LOGIN PAGE
    # Validate that the Login screen has been displayed
    assert login_page.get_login_title() == "Login", f"It should be in Login screen, but it is in {login_page.get_login_title()}"

    # Try to log in without entering Username and Password and validate the error in the Username field
    login_page.do_login()
    login_page.is_username_error_display()

    # Try to log in without entering Password and validate the error in the Password field
    login_page.fill_user(user)
    login_page.do_login()
    login_page.is_password_error_display()

    # Capture the first Username from the Usernames list and the password, login
    login_page.do_first_login_example()
    login_page.do_login()

    ### SHIPMENT ADDRESS PAGE
    # Validate that the Checkout, Shipment Address screen has been displayed
    assert address_page.get_title() == "Enter a shipping address", f"It should be in Shipping Address screen, but it is in {address_page.get_title()}"

    # PLUS: Validate all the required fields and their errors when trying to submit the payment without entering these fields
    address_page.go_to_payment()
    address_page.assert_is_all_errors_displayed()

    # Enter information in all the form fields and proceed to payment.
    address_page.fill_forms_completely(load_data)
    address_page.go_to_payment()

    ### PAYMENT METHOD PAGE

    # Validate that the Checkout, Payment screen has been displayed
    assert payment_page.get_title() == "Enter a payment method", f"It should be in Payment Method screen, but it is in {payment_page.get_title()}"

    # PLUS: Validate all mandatory fields.
    payment_page.go_to_review_order()
    payment_page.assert_is_all_card_errors_displayed()

    # Enter the values in the corresponding fields 
    payment_page.fill_forms_card(load_data)

    # PLUS: Uncheck the Checkbox and Validate all required fields and their errors when trying to submit the payment without entering these fields.
    if payment_page.is_checked_same_billing_address():
        payment_page.click_billing_address()
    payment_page.go_to_review_order()
    payment_page.assert_is_all_billing_adddress_errors_displayed()
    payment_page.fill_forms_billing_address(load_data)

    # Proceed to the review by clicking on the Review Order button
    payment_page.go_to_review_order()


    ### REVIEW YOUR ORDER PAGE

    # Validate that the Checkout, Review your order screen has been displayed.
    # Validate that the Deliver Address and Payment Method information is correct
    # Validate the product's unit information such as Name and Value
    # Validate that the total value of the items plus the Freight value is correct.
    # Click on the Place Order button

    
    # Validate that the Checkout Complete screen has been displayed
    # Click on the Continue Shopping button
    # Validate that the Products screen has been displayed and that the cart is empty.