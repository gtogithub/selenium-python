from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome
chromeDriverPath = r'D:\resources\chromedriver.exe'
chromeService = Service(chromeDriverPath)
driver = webdriver.Chrome(service=chromeService)

url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.maximize_window()
driver.get(url)

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Grzegorz")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
assert "Grzegorz" in alert.text
alert.accept()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Gregorio")
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
assert "Gregorio" in alert.text
alert.dismiss()
