import time

#Drives a browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 

class Scraper:
    
    def __init__(self, url, delay):
        self.url=url
        # Pause time after each scroll
        self.delay=delay
        
    def fetch_url(self):
        chrome_options = Options()
        # To make scrolling happen we need to add browser windows size
        chrome_options.add_argument("window-size=1920,1080") 
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        driver.get(self.url)

        # Allow scroll_pause_time seconds for initial webpage load
        time.sleep(self.delay) 
        
        return driver
        

class DivarScraper(Scraper):
    
    def __init__(self, url, delay, pagination_count):
        super().__init__(url, delay)
        self.pagination_count=pagination_count
    
    def scraper(self):
        driver=Scraper.fetch_url(self)
        # Loop counter
        i=1
        '''for on scroll endless pagination'''
        while i < self.pagination_count:
            # Scrape cards
            cards = driver.find_elements(By.CSS_SELECTOR, "div.post-list__widget-col-c1444")
            
            # Print count of items
            print("items: " + str(len(cards))) 

            for div in cards:
                # Card url
                #print(div.get_attribute('innerHTML')+'\n')
                try:
                    # Card Title
                    print(div.find_element(By.TAG_NAME, "h2").text+'\n') 
                    # Card URL
                    print(div.find_element(By.TAG_NAME, "a").get_attribute('href')) 
                    print('\n\n')
                except:
                    print('')
            

            # Print count of items again
            print("items: " + str(len(cards)))
            
            # Scroll one screen height each time
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            i += 1
            
        
        driver.quit()


divar=DivarScraper("https://divar.ir/s/karaj/car?q=%D8%AF%D9%86%D8%A7",4,4)
divar.scraper()
