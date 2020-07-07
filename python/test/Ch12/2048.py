#! python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
type(browser)
browser.get('https://gabrielecirulli.github.io/2048/')
time.sleep(5)
count=100
htmlElem = browser.find_element_by_tag_name('html')
for i in range(count):
    time.sleep(1)
    #Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
    htmlElem.send_keys(Keys.UP)
    time.sleep(1)
    htmlElem.send_keys(Keys.RIGHT)
    time.sleep(1)
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(1)
    htmlElem.send_keys(Keys.LEFT)
    if i%10 == 0:
        print(i)
print('done')