from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

chromeDriverPath = r'D:\resources\chromedriver.exe'
chromeService = Service(chromeDriverPath)
url = 'https://www.google.com/'

driver = webdriver.Chrome(service=chromeService)
driver.maximize_window()
driver.get(url)
driver.get(url + "doodles")
driver.back()
driver.refresh()
driver.forward()
