# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:37:25 2020

@author: Ch Salman  Gujjar
"""

from selenium import webdriver

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome()

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login')

# locate email form by_class_name
username = driver.find_element_by_class_name('input__field input__field--with-label')

username = driver.find_elements_by_xpath("//div[@class='login__form']/div[@class='form__input--floating']")
# send_keys() to simulate key strokes
username.send_keys('s777.msg@gmail.com')

# locate password form by_class_name
password = driver.find_element_by_class_name('input__field input__field--with-label')
password = driver.find_elements_by_xpath("//div[@class='login__form']/div[@class='form__input--floating']")
# send_keys() to simulate key strokes
password.send_keys(9279458)

log_in_button = driver.find_element_by_class_name('btn__primary--large from__button--floating')

# locate submit button by_class_id
log_in_button = driver.find_element_by_class_id('login submit-button')

# locate submit button by_xpath
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()


