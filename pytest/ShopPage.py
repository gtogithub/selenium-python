from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        
    products = (By.XPATH,"//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    buyButton = (By.XPATH, "div/button")
    checkoutButton = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    
    def get_products(self):
        return self.driver.find_elements(*ShopPage.products)
    
    def get_product_name(self, product):
        return product.find_element(*ShopPage.productName)
    
    def buy_product(self, product):
        return product.find_element(*ShopPage.buyButton)
    
    def select_checkout(self):
        return self.driver.find_element(*ShopPage.checkoutButton)