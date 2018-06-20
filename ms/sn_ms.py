from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://passport.suning.com/ids/login")

elemtab = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/a[2]/span")
elemtab.click()
elem = driver.find_element_by_id("userName")
elem.send_keys("17316901545")

elem2 = driver.find_element_by_id("password")
elem2.send_keys("asus135")
elem.send_keys(Keys.RETURN)
print(driver.page_source)
