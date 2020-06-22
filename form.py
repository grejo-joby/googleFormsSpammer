import time
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options # firefox
from selenium.webdriver.chrome.options import Options#chrome  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import json	
# My side of changes i did here

chrome_options = Options()
chrome_options.add_argument("--headless") 
driver=webdriver.Chrome(options=chrome_options)

for i in range(176,1000):
	driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeaiz2sFf6ssahlpf-VrYDRUbiq0VoVjhHwwcbUlquHRiaGZg/viewform')
	time.sleep(2)

	ele=driver.find_elements_by_xpath('//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
	ele[0].send_keys(i+1)
	ele[1].send_keys('email@gmail.com')


	submit=driver.find_element_by_xpath('//span[@class="appsMaterialWizButtonPaperbuttonContent exportButtonContent"]')
	submit.click()
