'''
Created on 17 Mar 2021

@author: shane
'''
import time

from bs4 import BeautifulSoup
from selenium import webdriver


login = 'http://localhost:8080/MYSERVER/login'
secret = 'http://localhost:8080/MYSERVER/secret'
driver = webdriver.Chrome(executable_path='/Users/shane/chromedriver')

driver.get(url=login);
time.sleep(1)
driver.get(url=secret);

txt = driver.page_source

soup = BeautifulSoup(txt, 'html.parser')
 
for info in soup.select('td'):
    print(info.text)