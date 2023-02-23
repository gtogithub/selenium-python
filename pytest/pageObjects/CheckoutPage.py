from selenium.webdriver.common.by import By
from pageObjects.DeliveryPage import DeliveryPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        
    checkoutButton = (By.XPATH,"//button[@class='btn btn-success']")
    
    def select_checkout(self):
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        deliveryPage = DeliveryPage(self.driver)
        return deliveryPage
        
