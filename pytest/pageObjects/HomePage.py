from selenium.webdriver.common.by import By
from pageObjects.ShopPage import ShopPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    
    shopLink = (By.CSS_SELECTOR, "a[href*='shop']")
    
    def go_to_shop(self):
        self.driver.find_element(*HomePage.shopLink).click()
        shopPage = ShopPage(self.driver)
        return shopPage