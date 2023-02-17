from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("-headless")

firefoxDriverPath = r'D:\resources\geckodriver.exe'
firefoxService = Service(firefoxDriverPath)
driver = webdriver.Firefox(service=firefoxService, options=firefox_options)

url = "https://tvn.pl"
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(3)

# cookies consent
try:
    driver.find_element(By.CSS_SELECTOR, "button[id='onetrust-accept-btn-handler']").click()
except:
    print("No cookies consent window")

   
# scroll to the bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# take a screenshot
driver.get_screenshot_as_file("D://screenshot.png")

print("Script has been executed with firefox in headless mode")
