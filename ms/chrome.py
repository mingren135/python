from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

def getChrome():
  option = webdriver.ChromeOptions()
  option.add_argument('disable-infobars')

  # 打开chrome浏览器
  driver = webdriver.Chrome(chrome_options=option)
  return driver
