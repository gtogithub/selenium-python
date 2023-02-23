from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.DeliveryPage import DeliveryPage
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage


class TestOne(BaseClass):
    # first test case
    def test_buy_blackberry(self):
        
        driver = self.driver
        driver.implicitly_wait(4)
        
        homePage = HomePage(driver)
        shopPage = homePage.go_to_shop()
        products = shopPage.get_products()

        for product in products :
            productName = shopPage.get_product_name(product).text
            if productName == "Blackberry":
                shopPage.buy_product(product).click()

        checkoutPage = shopPage.select_checkout()
        deliveryPage = checkoutPage.select_checkout()
        deliveryPage.insert_location().send_keys("pol")
        wait = WebDriverWait(driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Poland")))
        deliveryPage.choose_location().click()
        deliveryPage.select_checkbox().click()
        deliveryPage.purchase().click()
        successText = deliveryPage.get_confirmation().text
        assert "Success! Thank you!" in successText