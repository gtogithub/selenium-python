from selenium.webdriver.common.by import By


class DeliveryPage:
    def __init__(self, driver):
        self.driver = driver
        
    locationField = (By.ID,"country")
    locationPoland = (By.LINK_TEXT,"Poland")
    checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR,"[type='submit']")
    successText = (By.CLASS_NAME,"alert-success")
    
    def insert_location(self):
        return self.driver.find_element(*DeliveryPage.locationField)
    
    def choose_location(self):
        return self.driver.find_element(*DeliveryPage.locationPoland)
    
    def select_checkbox(self):
        return self.driver.find_element(*DeliveryPage.checkbox)
    
    def purchase(self):
        return self.driver.find_element(*DeliveryPage.purchaseButton)
    
    def get_confirmation(self):
        return self.driver.find_element(*DeliveryPage.successText)