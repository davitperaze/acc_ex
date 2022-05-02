from testlib.pages.basepage import BasePage as BP
from testlib.locators.page_locators import PageLocators as PL

import allure


class AllPages(BP):
    def __init__(self):
        pass

    @allure.step("Click mobile category")
    def click_mobile_category(self):
        mobile_category = BP.find_element(self, PL.MOBILE_CATEGORY)
        mobile_category.click()

    @allure.step("Open sorter drop down")
    def click_sorter(self):
        sorter = BP.find_element(self, PL.SORTER_DROPDOWN)
        sorter.click()

    @allure.step("Click Price descending")
    def click_price_desc(self):
        price_desc = BP.find_element(self, PL.PRICE_DESC)
        price_desc.click()

    @allure.step("Click add to cart")
    def click_add_to_cart_1(self):
        mobile_category = BP.find_element(self, PL.ADD_TO_CART_1)
        mobile_category.click()
    @allure.step("Click add to cart")
    def click_add_to_cart_2(self):
        mobile_category = BP.find_element(self, PL.ADD_TO_CART_2)
        mobile_category.click()

    @allure.step("Count cart items")
    def check_cart_cuantity(self):
        cart_quantity = BP.find_element(self, PL.HEADER_CART_COUNTER)
        return cart_quantity.text
