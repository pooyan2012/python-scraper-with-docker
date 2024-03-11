import time

#drives a browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://divar.ir/'

driver.get(url)

# Find all the div elements on the page
div_elements = driver.find_elements(By.TAG_NAME, "div")
# Extract the text from each div element
divs = [div.text for div in div_elements]
# Print the list of titles
print(divs)

time.sleep(10)

driver.quit()
