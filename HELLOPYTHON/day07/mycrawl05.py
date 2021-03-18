'''
Created on 17 Mar 2021

@author: shane
'''
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


URL = 'http://localhost:8080/MYSERVER/login'
driver = webdriver.Chrome(executable_path='/Users/shane/chromedriver')
driver.get(url=URL);
 
response = requests.get('http://localhost:8080/MYSERVER/secret')
txt = response.text

# print(txt)
 
soup = BeautifulSoup(txt, 'html.parser')
 
for info in soup.select('td'):
    print(info.text)