'''
Created on 17 Mar 2021

@author: shane
'''
import requests
from bs4 import BeautifulSoup
 
response = requests.get('https://www.sedaily.com/Stock/quote')
 
txt = response.text
soup = BeautifulSoup(txt, 'html.parser')
 
stockNames = []
stockPrices = []
for info in soup.select('dl'):
    
    
    dlTags = info.select('dl');
    
    aTags = info.select('a');
    
    for aTag in aTags:
        name = aTag.text
        if(len(name) > 0):
            stockNames.append(name)
    
    spanTags = info.select('span');
    
    for span in spanTags:
        price = span.text.replace(",","")
        stockPrices.append(price)
        break;
    
print(stockNames)
print(stockPrices)
   
   
