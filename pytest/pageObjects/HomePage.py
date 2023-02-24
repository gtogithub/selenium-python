from selenium.webdriver.common.by import By
from pageObjects.ShopPage import ShopPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    
    shopLink = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    checkbox = (By.CLASS_NAME, "form-check")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    
    
    def go_to_shop(self):
        self.driver.find_element(*HomePage.shopLink).click()
        shopPage = ShopPage(self.driver)
        return shopPage
    
    def get_name(self):
        return self.driver.find_element(*HomePage.name)
    
    def get_email(self):
        return self.driver.find_element(*HomePage.email)
    
    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)
    
    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)
    
    def submit_form(self):
        return self.driver.find_element(*HomePage.submit)

    def get_message(self):
        return self.driver.find_element(*HomePage.successMessage)