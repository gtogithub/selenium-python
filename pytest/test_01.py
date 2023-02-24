import pytest
from BaseClass import BaseClass
from TestData import TestData
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_buy_blackberry(self, get_data):
        
        driver = self.driver
        driver.implicitly_wait(4)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        
        homePage = HomePage(driver)
        shopPage = homePage.go_to_shop()
        products = shopPage.get_products()

        for product in products :
            productName = shopPage.get_product_name(product).text
            if productName == "Blackberry":
                shopPage.buy_product(product).click()

        checkoutPage = shopPage.select_checkout()
        deliveryPage = checkoutPage.select_checkout()
        deliveryPage.insert_location().send_keys(get_data["firstLetters"])
        self.verify_link_presence(get_data["countryLink"])
        deliveryPage.choose_location().click()
        deliveryPage.select_checkbox().click()
        deliveryPage.purchase().click()
        successText = deliveryPage.get_confirmation().text
        assert "Success! Thank you!" in successText

    @pytest.fixture(params=TestData.data1)        
    def get_data(self, request):
        return request.param