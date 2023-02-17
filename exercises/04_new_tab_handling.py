from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Firefox
firefoxDriverPath = r'D:\resources\geckodriver.exe'
firefoxService = Service(firefoxDriverPath)
driver = webdriver.Firefox(service=firefoxService)

url = "https://tvn.pl"
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(3)

# cookies consent
try:
    driver.find_element(By.CSS_SELECTOR, "button[id='onetrust-accept-btn-handler']").click()
except:
    print("No cookies consent window")

# wait = WebDriverWait(driver, 4)
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a[title='eurosport-1'] svg")))

# close any pop-up window
try:
    driver.find_element(By.CSS_SELECTOR, "div[id='closeButton']").click()
except:
    print("")
    
# open a new tab
driver.find_element(By.CSS_SELECTOR, "a[title='eurosport-1'] svg").click()

windows = driver.window_handles
# switching to child tab
driver.switch_to.window(windows[1])

# cookies consent - child tab
try:
    driver.find_element(By.CSS_SELECTOR, "button[id='onetrust-accept-btn-handler']").click()
except:
    print("No cookies consent window")
    
print("Eurosport 1 hot topic: ", driver.find_element(By.CSS_SELECTOR, ".urgent-article__title").text)
driver.close()
driver.switch_to.window(windows[0])
print("TVN top story: ", driver.find_element(By.CSS_SELECTOR, "header[class='top-story__header'] h2").text)