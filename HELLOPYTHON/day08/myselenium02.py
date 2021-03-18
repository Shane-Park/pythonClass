'''
Created on 17 Mar 2021

@author: shane
'''
import time

from bs4 import BeautifulSoup
from selenium import webdriver


login = 'http://localhost:8080/MYSERVER/login.html'
secret = 'http://localhost:8080/MYSERVER/secret'
driver = webdriver.Chrome(executable_path='/Users/shane/chromedriver')

driver.get(login)
driver.find_element_by_name('id').send_keys('president')
driver.find_element_by_name('pw').send_keys('password')
time.sleep(1.5)

driver.find_element_by_id('mysubmit').click()
time.sleep(1)
driver.get(secret)

txt = driver.page_source
soup = BeautifulSoup(txt, 'html.parser')

for info in soup.select('td'):
    print(info.text)