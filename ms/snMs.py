from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
from chrome import getChrome

def login(driver, nick, password):
  driver.get("https://passport.suning.com/ids/login")

  elemtab = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/a[2]/span")
  elemtab.click()
  elem = driver.find_element_by_id("userName")
  elem.send_keys(nick)

  elem2 = driver.find_element_by_id("password")
  elem2.send_keys(password)

  time.sleep(2)
  print('sleep 2s')
  elem.send_keys(Keys.RETURN)
  print('login success, nick:%s' % nick)

def buy(driver, itemId):
  urlTemplate = 'https://product.suning.com/0000000000/{itemId}.html'
  itemUrl = urlTemplate.replace('{itemId}', itemId)
  driver.get(itemUrl)
  buyNowElem = driver.find_element_by_id("buyNowAddCart")
  
  time.sleep(5)
  print('sleep 5s')
  buyNowElem.click()
  print('buyNow clicked, itemId:%s' % itemId)
  
  time.sleep(5)  
  print('sleep 5s')
  submitElem = driver.find_element_by_id("submit-btn")
  submitElem.click()
  #print('submit clicked, itemId:%s' % itemId)

def buyApi(driver, itemId, quantity=1):
   

if __name__ == '__main__':
  if len(sys.argv) < 3:
    print('must input nick&password')
  
  driver = getChrome()
  nick = sys.argv[1]
  password = sys.argv[2]
  login(driver, nick, password)
  
  itemId = sys.argv[3]
  buy(driver, itemId)
  #print(driver.page_source)
