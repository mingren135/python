#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import ssl
from bs4 import BeautifulSoup  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from product import Product


def findSnItemPrice(product):
  urlTemplate = 'https://product.suning.com/0000000000/{itemId}.html'
  itemId = product.getProdId()
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
  itemStatusList = bsObj.select("#haveProduct")
  itemStatus = itemStatusList[0].get_text()
  if itemStatus.strip() == '':
    kucunStatusList = bsObj.select("#c_kucun")
    itemStatus = kucunStatusList[0].get_text()
  print("itemStatus:%s" % itemStatus)

  mjPromDescList = bsObj.select("#voucherBox")
  mjPromDesc = mjPromDescList[0].get_text()
  #print(priceList)
  #print(itemNameList)
  if len(priceList)>0:
    for price in priceList:  
      strPrice = price.get_text().replace('¥','').replace('.00','').replace(' ','')
  else:
      strPrice = "-1"
  
  product.printProd()
  print("price:%s,name:%s,desc:%s,mjProm:%s" % (strPrice, itemName, promDesc, mjPromDesc))

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('arguments at least 1')
    print('usage: python3 pollSnProdPrice.py snProdIds.txt')
    sys.exit()
  
  dict = {}
  prodKeys = []
  fileName = sys.argv[1]
  with open(fileName) as f:
    for line in f:
      if line.startswith('#'):
        prodKey = line.strip('#').strip('\n')
        prodKeys.append(prodKey)
        prods = []
        dict[prodKey] = prods
        continue
      #print('line:%s' % line)
      prods.append(Product(line.strip('\n')))

  #print("dict:%s" % dict)
  for prodKey in prodKeys:
    print('------------------------------%s' % prodKey)
    prods = dict[prodKey]
    for prod in prods:
      findSnItemPrice(prod)
      print('')
