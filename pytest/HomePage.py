from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    
    shopLink = (By.CSS_SELECTOR, "a[href*='shop']")
    
    def go_to_shop(self):
        return self.driver.find_element(*HomePage.shopLink)