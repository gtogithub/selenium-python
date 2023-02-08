from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

# Chrome
chromeDriverPath = r'D:\resources\chromedriver.exe'
chromeService = Service(chromeDriverPath)
driver = webdriver.Chrome(service=chromeService)

# Firefox
firefoxDriverPath = r'D:\resources\geckodriver.exe'
firefoxService = Service(firefoxDriverPath)
#driver = webdriver.Firefox(service=firefoxService)

# Edge
edgeDriverPath = r'D:\resources\msedgedriver.exe'
edgeService = Service(edgeDriverPath)
#driver = webdriver.Edge(service=edgeService)

url = 'https://www.google.com/'


driver.maximize_window()
driver.get(url)
driver.get(url + "doodles")
driver.back()
driver.refresh()
driver.forward()
