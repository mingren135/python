#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import ssl
from urllib.request import urlopen  
from urllib.request import Request
from bs4 import BeautifulSoup  

webheader = {  
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',  
  'Accept-Language': 'zh-CN',  
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',  
  'Connection': 'Keep-Alive',  
  'Host': 'product.suning.com'  
}

urlTemplate = 'https://product.suning.com/0000000000/{itemId}.html'

def findSnItemPrice(itemId):
  itemUrl = urlTemplate.replace('{itemId}', str(itemId))
  #print("itemUrl=%s" % itemUrl)

  req = Request(url=itemUrl,headers=webheader) 
  context = ssl._create_unverified_context()
  html = urlopen(req, context=context)
  print(html.read().decode('utf-8'))  

  bsObj = BeautifulSoup(html,"html.parser")
  priceList=bsObj.findAll("span",{"class":"zy"})  
  print(priceList)
  for price in priceList:  
       print("price:%" % price.get_text())  

if len(sys.argv)<0:
  print('arguments at least 1')

findSnItemPrice(sys.argv[1])
