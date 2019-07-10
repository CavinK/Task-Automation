# Facebook Auto Poster with Selenium and Python 

from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep 
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get('http://facebook.com')

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f: # ID and PW saved on this text file 
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw

email, password = read_creds()

# Copy Xpath from the webpage(inspection)
emailelement = driver.find_element(By.XPATH, './/*[@id="email"]') # be careful on quotation marks and the period! 
emailelement.send_keys(email) # use your own email address! 
passelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passelement.send_keys(password)

# Clicking the log in button 
elem = driver.find_element(By.XPATH, './/*[@id="loginbutton"]') # the actual XPath of the button 
elem.click() 

statuselement = driver.find_element(By.XPATH, './/*[@name="xhpc_message"]') # to express your status 
time.sleep(5) 

statuselement.send_keys('Hey buddies') 
time.sleep(5) 

# Post button 
buttons = driver.find_element_by_tag_name('button') 
time.sleep(5)

for button in buttons: 
	if button.text == 'Post': 
		button.click() 
