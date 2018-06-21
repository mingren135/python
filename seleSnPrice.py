#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import ssl
from bs4 import BeautifulSoup  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


urlTemplate = 'https://product.suning.com/0000000000/{itemId}.html'

def findSnItemPrice(itemId):
  itemUrl = urlTemplate.replace('{itemId}', str(itemId))
  #print("itemUrl=%s" % itemUrl)
  

  #driver = webdriver.PhantomJS()
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')
  driver = webdriver.Chrome(chrome_options=chrome_options)
  driver.get(itemUrl)
  html = driver.page_source
  #print(html)  

  bsObj = BeautifulSoup(html,"html.parser")
  priceList=bsObj.findAll("span",{"class":"mainprice"})  
  itemNameList = bsObj.findAll("h1", {"id":"itemDisplayName"})
  itemName = itemNameList[0].get_text()
  promDescList = bsObj.findAll("h2", {"id":"promotionDesc"})
  promDesc = promDescList[0].get_text()
  #print(priceList)
  #print(itemNameList)
  for price in priceList:  
    strPrice = price.get_text().replace('¥','').replace('.00','')
    print("itemId=%s,price:%d,itemName:%s,promDesc:%s" % (itemId,int(strPrice), itemName, promDesc))

if len(sys.argv)<0:
  print('arguments at least 1')

lines = []
with open('sn8pIds.txt') as f:
  lines = f.readlines()
print(lines)

if len(sys.argv)>1:
  findSnItemPrice(sys.argv[1])
else:
  for itemId in lines:
    itemId = itemId.strip('\n')
    findSnItemPrice(itemId)
