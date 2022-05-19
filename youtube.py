import urllib
import urllib.request as urllib2
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#path to executable
driver = webdriver.Chrome(options=option, executable_path=r'C:\chromedriver_win32\chromedriver.exe') 
driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(5)

# search Youtube Video
search = driver.find_element_by_name('search_query')
search.click()
sleep(3)
driver.find_element_by_name('search_query').send_keys('Around The World Around The World')
driver.find_element_by_id("search-icon-legacy").click()
sleep(5)
driver.find_element_by_class_name("style-scope ytd-video-renderer").click()
sleep(30)


#now you can refresh the page!
driver.refresh()
sleep(30)

   
print ("Done")
input('You can type quit to exist')
driver.quit()
