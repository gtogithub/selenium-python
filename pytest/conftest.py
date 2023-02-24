from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class") 
def browser_setup(request):
    
    browser_name = request.config.getoption("browser_name")
    
    if browser_name == "chrome":
        chromeDriverPath = r'D:\resources\chromedriver.exe'
        chromeService = Service(chromeDriverPath)
        driver = webdriver.Chrome(service=chromeService)
    elif browser_name == "firefox":
        firefoxDriverPath = r'D:\resources\geckodriver.exe'
        firefoxService = Service(firefoxDriverPath)
        driver = webdriver.Firefox(service=firefoxService)
    elif browser_name == "edge":
        edgeDriverPath = r'D:\resources\msedgedriver.exe'
        edgeService = Service(edgeDriverPath)
        driver = webdriver.Edge(service=edgeService)
        
    driver.maximize_window()
    request.cls.driver = driver
    
    yield
    # browser tear down
    driver.close()
