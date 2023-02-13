import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Chrome
chromeDriverPath = r'D:\resources\chromedriver.exe'
chromeService = Service(chromeDriverPath)
driver = webdriver.Chrome(service=chromeService)

url = "https://rahulshettyacademy.com/seleniumPractise/#/"
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(4)


driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
products = driver.find_elements(By.CSS_SELECTOR, "div[class='product']")

assert (len(products)) > 0 

for product in products:
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a[@class='cart-icon']/img").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

assert "Code applied" in driver.find_element(By.CSS_SELECTOR, ".promoInfo").text


