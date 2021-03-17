'''
Created on 17 Mar 2021

@author: shane
'''
import requests
from bs4 import BeautifulSoup
 
response = requests.get('https://www.sedaily.com/Stock/quote')
 
txt = response.text
soup = BeautifulSoup(txt, 'html.parser')
 
for info in soup.select('.tbody'):
    name = info.dt.text
    price = info.dd.span.text.replace(",","")
    stockId = info.dd['id']
    stockId = stockId[-6:len(stockId)]
    print(name, end='\t')
    print(price, end='\t')
    print(stockId)
   
