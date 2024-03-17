import time

#Drives a browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 

def scraper(driver):
    # Scrape cards
    cards = driver.find_elements(By.CSS_SELECTOR, "div.post-list__widget-col-c1444")
    
    # Print count of items
    print("items: " + str(len(cards))) 

    for div in cards:
        # Card url
        print(div.get_attribute('innerHTML')+'\n')
        print(div.find_element(By.TAG_NAME, "a").get_attribute('href')) 
        print(div.find_element(By.TAG_NAME, "h2").text+'\n\n') 
        #print(div.get_attribute('innerHTML')+'\n\n')
    

    # Print count of items again
    print("items: " + str(len(cards)))

chrome_options = Options()
# To make scrolling happen we need to add browser windows size
chrome_options.add_argument("window-size=1920,1080") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://divar.ir/s/karaj/car?q=%D8%AF%D9%86%D8%A7'

driver.get(url)

# Allow 2 seconds for initial webpage load
time.sleep(2) 
'''**********************************************'''
# Pause time after each scroll
scroll_pause_time = 2 
# Get the screen height
screen_height = driver.execute_script("return window.screen.height;")   

i=1
end_index=3

'''for on scroll endless pagination'''
while i < end_index:
    '''there is a bug here that it doesnt 
    scrape first page and if i add scraper 
    before  scroll i get error'''
    # Scroll one screen height each time
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i += 1
    # Allow scroll_pause_time seconds for webpage load
    time.sleep(scroll_pause_time)

    scraper(driver)

'''**********************************************'''


time.sleep(10)

driver.quit()
