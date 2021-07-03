from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import time
#创建浏览器
#driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver = webdriver.Chrome()

driver.get("https://www.winxuan.com/")

WebDriverWait(driver,2,0.5).until(lambda el:el.find_element_by_link_text("我的文轩"))

navbtn = driver.find_element_by_link_text("我的文轩")
#鼠标移动
ActionChains(driver).move_to_element(navbtn).perform()

driver.find_element_by_xpath("//*[@id='common-sys-head1210-2020_default']/div[2]/div/ul[2]/li[1]/div/ul/li[1]/a").click()
#针对地图拖拽
'''
第一步：找到元素
第二步：实例化ActionChains对象
第三步：移动到这个元素，拖拽，偏移，释放
'''
# for i in range(10):
#     mask = driver.find_element_by_id('mask')
#     action = ActionChains(driver)
#     action.move_to_element(mask).click_and_hold().move_by_offset(50,30).release().perform()
