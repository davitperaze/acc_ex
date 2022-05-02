
import pytest
import allure
from testlib.pages.allpages import AllPages

AP = AllPages()
import time

@allure.feature("zoommer.ge add to cart")
@allure.story("Happy path testing")
class TestAddToCart:
    @allure.title("Go to mobile phones category")
    @allure.description("")
    def test_go_to_mobiles(self):
        """Test Home Page is loaded"""
        AP.click_mobile_category()

    @allure.title("Sort items by price from high to low")
    @allure.description("???")
    def test_sort_price_desc(self):
        """Check back button visibility"""
        AP.click_sorter()
        AP.click_price_desc()

    @allure.title("Add first item to cart")
    @allure.description("...")
    def test_add_to_cart(self):
        AP.click_add_to_cart_1()
    @allure.title("Add second item to cart")
    @allure.description("...")
    def test_add_second_to_cart(self):
        AP.click_add_to_cart_2()

    @allure.title("Check cart quantity")
    @allure.description("")
    def test_cart_quantity(self):
        assert AP.check_cart_cuantity() == "2"

