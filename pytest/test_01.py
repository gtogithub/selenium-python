from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.mark.usefixtures("browser_setup")
class TestOne:
    # first test case
    def test_buy_blackberry(self):
        driver = self.driver
        driver.implicitly_wait(4)
        driver.find_element(By.CSS_SELECTOR," a[href*='shop']").click()
        products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

        for product in products :
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        driver.find_element(By.ID,"country").send_keys("pol")
        wait = WebDriverWait(driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Poland")))
        driver.find_element(By.LINK_TEXT,"Poland").click()
        driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        successText = driver.find_element(By.CLASS_NAME,"alert-success").text
        assert "Success! Thank you!" in successText