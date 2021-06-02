from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver.get('https://google.com')

# driver.find_element_by_name('q').send_keys('اموزش python' + Keys.ENTER)

# driver.find_element_by_name('q').send_keys('اموزش python')
# driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)

# driver.get('https://cmder.net/')
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,700)')

driver.get('https://instagram.com')
driver.find_element_by_xpath('//input[@name="username"]').send_keys('Mohamad Reza Safari')
