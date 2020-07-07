# from selenium import webdriver
# browser = webdriver.Firefox()
# type(browser)
# browser.get('https://inventwithpython.com')

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://inventwithpython.com')
# try:
#     elem = browser.find_element_by_class_name('cover-thumb')
#     print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://inventwithpython.com')
# linkElem = browser.find_element_by_link_text('Read Online for Free')
# type(linkElem)
# linkElem.click() # follows the "Read Online for Free" link

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://login.metafilter.com')
# userElem = browser.find_element_by_id('user_name')
# userElem.send_keys('your_real_username_here')

# passwordElem = browser.find_element_by_id('user_pass')
# passwordElem.send_keys('your_real_password_here')
# passwordElem.submit()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# browser = webdriver.Firefox()
# browser.get('https://nostarch.com')
# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END)     # scrolls to bottom
# htmlElem.send_keys(Keys.HOME)    # scrolls to top