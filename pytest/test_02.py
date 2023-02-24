import pytest
from TestData import TestData
from pageObjects.HomePage import HomePage
from BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        driver = self.driver
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        homePage= HomePage(self.driver)
        homePage.get_name().send_keys(getData["name"])
        homePage.get_email().send_keys(getData["email"])
        homePage.get_checkbox().click()
        self.selectOptionByText(homePage.get_gender(), getData["gender"])

        homePage.submit_form().click()

        alertText = homePage.get_message().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=TestData.data2)
    def getData(self, request):
        return request.param

