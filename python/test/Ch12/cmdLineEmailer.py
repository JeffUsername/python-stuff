#! python3
import sys, time
import pyinputplus as pyip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#get cmd line parts
toWhom = sys.argv[1]
subject = sys.argv[2]
body = sys.argv[3:]
pwpart = pyip.inputPassword('Enter password: ') #password enter

#get to site, input username
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
#time.sleep(5)
userElem = browser.find_element_by_id('identifierId')
userElem.send_keys('thingforprogrammingbook@gmail.com')
#linkElem = browser.find_element_by_id('ZFr60d CeoRYc')
linkElem = browser.find_element_by_id('identifierNext')
type(linkElem)
linkElem.click()
#enter password
passwordElem = browser.find_element_by_class_name('password')
passwordElem.send_keys(pwpart)
passwordElem.submit()

print('Done')
