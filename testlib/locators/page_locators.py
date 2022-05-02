from selenium.webdriver.common.by import By


class PageLocators:
    MOBILE_CATEGORY = (
        By.XPATH,
        '//div[@class="navigation"]//a[contains(@href, "/mobilurebi-2")]',
    )
    SORTER_DROPDOWN = (
        By.XPATH,
        '//div[contains(@class,"sorter_dropdown")]//button[@data-toggle="dropdown"]',
    )
    PRICE_DESC = (By.XPATH, '//a[contains(@href, "orderby=11")]')
    ADD_TO_CART_1 = (By.XPATH, '/html/body/div[7]/section/div[4]/div[1]/div[4]/div[2]/div/div[1]/div[1]/div/div[2]/div[2]/div')
    ADD_TO_CART_2 = (By.XPATH, '/html/body/div[7]/section/div[4]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div')
    HEADER_CART = (
        By.XPATH,
        '//div[contains(@class, "header_basket not_for_portrait_mobile topcartlink")]',
    )
    HEADER_CART_COUNTER = (
        By.XPATH,
        '//div[@class="h_basket_title_price"]//div[contains(@class, "js_basket_count")]',
    )
