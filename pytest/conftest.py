from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(scope="class") 
def browser_setup(request):
    # Chrome
    chromeDriverPath = r'D:\resources\chromedriver.exe'
    chromeService = Service(chromeDriverPath)

    # Firefox
    firefoxDriverPath = r'D:\resources\geckodriver.exe'
    firefoxService = Service(firefoxDriverPath)

    # Edge
    edgeDriverPath = r'D:\resources\msedgedriver.exe'
    edgeService = Service(edgeDriverPath)

    # Choose which browser you want to use - leave selected option uncommented
    driver = webdriver.Chrome(service=chromeService)
    #driver = webdriver.Firefox(service=firefoxService)
    #driver = webdriver.Edge(service=edgeService)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    
    request.cls.driver = driver
    
    yield
    # browser tear down
    driver.close()
