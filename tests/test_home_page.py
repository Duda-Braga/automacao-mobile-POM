import pytest
import time 
from pages.home_page import HomePage
from pages.product_page import ProductPage
# Import other page objects as needed

def test_product_selection(driver):
    # Initialize page objects with the driver provided by the fixture
    home_page = HomePage(driver)
    product_page = ProductPage(driver)

    # Perform actions using page object methods
    assert home_page.get_home_page_title() == "Products"
    home_page.select_orange_backpack()

    # Continue with product page interactions
    # validate the correct product page oppended
    time.sleep(1)
    assert product_page.get_product_page_title() == "Sauce Labs Backpack (orange)"
    
    # Decrease qtt '-' and validate that the quantity has decreased by 1 unit
    inicial_value = product_page.get_product_quantity()
    product_page.decrease_qunatity()
    new_value = product_page.get_product_quantity()
    assert new_value ==  inicial_value-1, f"Quantity did not decrease, it should be {inicial_value - 1} but is {new_value}"

    # validate zero quantity of products the Add to cart button will become inactive.
    if new_value > 0:
        product_page.decrease_quantity_untill_X(0)
    assert not product_page.is_add_cart_clickable(), "Add to cart button should not work"
    
    # increase the quantity for 2 units and check if the add to cart button is enable then click it
    product_page.increase_quantity_untill_X(2)
    final_value = product_page.get_product_quantity()
    assert final_value == new_value+2, "It should increase 2 itens"
    product_page.add_to_cart()

    # Validate that a circle has appeared in the cart icon informing you of the exact number of items you have added to the cart
    assert product_page.get_cart_quantity() == final_value, f"Wrong qunatity in the cart it should be {final_value}"
    
    #open the cart
    product_page.go_to_cart()
    time.sleep(1)