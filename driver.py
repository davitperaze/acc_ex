from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options


class Driver:
    options = Options()
    options.add_argument("--headless")

    driver = wb.Chrome("chromedriver", options=options)

    driver.set_window_size(1440, 768)
    driver.get("https://zoommer.ge/")
    driver.implicitly_wait(10)
