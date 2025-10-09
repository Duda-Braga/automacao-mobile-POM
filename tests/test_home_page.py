import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.myCart_page import MyCart
# Import other page objects as needed

# Test test to purchase 1 type of item
def test_product_selection(driver):

    # Initialize page objects with the driver provided by the fixture
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    mycart_page = MyCart(driver)

    # item of test
    expected_product_name = "Sauce Labs Backpack (orange)"
    expeected_product_quantity = 2
    expected_unity_value = product_page.get_product_unity_value()
    expeted_total_item_value = expected_unity_value * expeected_product_quantity


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

    # Validate that the Login screen has been displayed
    # Try to log in without entering Username and Password and validate the error in the Username field
    # Try to log in without entering Password and validate the error in the Password field
    # Capture the first Username from the Usernames list at the bottom of the screen and enter this value in the Username field
    # Capture the Password from the Password list at the bottom of the screen and enter this value in the Password field
    # Click on the Login button