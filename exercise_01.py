from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

# Chrome
chromeDriverPath = r'D:\resources\chromedriver.exe'
chromeService = Service(chromeDriverPath)
driver = webdriver.Chrome(service=chromeService)

url = "https://ultimateqa.com/simple-html-elements-for-automation/"

driver.maximize_window()
driver.get(url)

driver.find_element(By.XPATH, "//input[@data-original_id='name']").send_keys("Tester")
driver.find_element(By.XPATH, "//input[@data-original_id='email']").send_keys("tester@tester.pl")
driver.find_element(By.XPATH, "//button[@class='et_pb_contact_submit et_pb_button']").click()

message = driver.find_element(By.XPATH, "//div[@class='et-pb-contact-message']/p").text
#assert "Thanks for contacting us" in message


url2 = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url2)

driver.find_element(By.CSS_SELECTOR, "input[id='autocomplete']").send_keys("pol")
sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] div")


for country in countries:
    if country.text == "Poland":
        country.click()
        break
    
assert driver.find_element(By.CSS_SELECTOR, "input[id='autocomplete']").get_attribute("value") == "Poland"
