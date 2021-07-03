from selenium import webdriver
from basePage.base_page import Tools
from selenium.webdriver.common.by import By

driver = Tools(webdriver.Chrome())
url = 'https://www.winxuan.com/'
driver.open(url)
driver.implicitlyWaitFun()
driver.clear((By.NAME,'keyword'))
driver.input((By.NAME,'keyword'),'故事会')

#对应不同的页面
