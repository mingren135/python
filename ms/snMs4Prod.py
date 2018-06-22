from chrome import getChrome
from snMs import login
from snMs import buy
import sys

if __name__ == "__main__":
  print('init account & password') 
  accounts = [] 
  with open('snAccount.txt') as f:
    for line in f:
      if line.startswith('#'):
        continue
      #print('line:%s' % line)
      accounts.append(line.strip('\n'))
  
  if len(sys.argv) <1:
     print('must input itemId')
  
  itemId = sys.argv[1]
  print('start to login and buy, itemId:%s', itemId)
  for account in accounts:
    nick = account.split(',')[0]
    password = account.split(',')[1]
    
    driver = getChrome()
    login(driver, nick, password)
    buy(driver, itemId)
  print('done')
