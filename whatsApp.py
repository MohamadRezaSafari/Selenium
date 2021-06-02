from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

msg = input('Enter msg  : ')
num = int(input('Enter enum : '))
name = input('Enter names : ')
names = name.split(',')

for i in names:
    user = driver.find_element_by_xpath(f'//span[@title="{i}"]')
    user.click()
    msg2 = driver.find_element_by_class_name('_2A8P4')
    for j in range(num):
        msg2.send_keys(msg)
        driver.find_element_by_class_name('_1E0Oz').click()



