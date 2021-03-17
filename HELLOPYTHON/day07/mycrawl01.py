'''
Created on 17 Mar 2021

@author: shane
'''
import requests
from bs4 import BeautifulSoup
 
response = requests.get('http://localhost:8080/MYSERVER/secret.html')
 
txt = response.text

# print(txt)
 
soup = BeautifulSoup(txt, 'html.parser')
 
for info in soup.select('td'):
    print(info.text)