'''
Created on 17 Mar 2021

숙제 1 parsing 하기
title, description, bloggername, bloggerlink, postdate

@author: shane
'''

import urllib.request

from bs4 import BeautifulSoup

client_id = "OQIdSmfOapYv43N94rCU"
client_secret = "1wnuSLskvs"
encText = urllib.parse.quote("테슬라")
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/news.xml?display=100&sort=date&query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    body = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
soup = BeautifulSoup(body, 'xml')

for info in soup.select('item'):
    print('title : ',info.title.text)
    print('description : ',info.description.text)
    print('pubDate : ',info.pubDate.text)
    print('link : ',info.link.text)
    print()
    
