from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time

class Browser :
    
    def __init__(self) :
        
        driverPath = "/home/ubuntu/chromedriver"
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(driverPath,chrome_options=chrome_options)
        
    def WaifForLoadPage(self,url) :
        self.browser.get(url)
        time.sleep(2)
    
    def PutData(self,data) : 
        search_box = self.browser.find_element(By.XPATH,"/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/input")
        search_box.send_keys(data)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        
        res = self.browser.find_element(By.XPATH,"/html/body/form/table/tbody/tr[5]/td/table/tbody/tr/td").text
        
        self.browser.quit()
        
        return res
        
        