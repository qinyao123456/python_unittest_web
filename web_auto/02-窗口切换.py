from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
driver= webdriver.Chrome()

driver.get("https://www.winxuan.com/")
time.sleep(2)
driver.find_element_by_name("keyword").clear()
driver.find_element_by_name("keyword").send_keys("故事会")
#通过class_name查找元素，class属性值有两个，是由空格隔开的，只能取一个
driver.find_element_by_class_name("master-search-btn").click()
#增加显示等待
WebDriverWait(driver,2,0.5).until(lambda el:el.find_element_by_xpath("//*[@id='grid']/li/ul/li[1]/div/div[1]/a/img"))
driver.find_element_by_xpath("//*[@id='grid']/li/ul/li[1]/div/div[1]/a/img").click()


#切换窗口
#获取当前所有的窗口
windows = driver.window_handles
driver.switch_to.window(windows[-1])   #切换到新打开的窗口
driver.find_element_by_id("addtocart").click()

driver.switch_to.window(windows[0])    #切换到第一个窗口

#切换到iframe
#找到frme
# frame = driver.find_element_by_id("frame")
# driver.switch_to.frame(frame)
# driver.find_element_by_id('nick').send_keys('nihao')
#跳出frame
#driver.switch_to.default_content()

#alert

alert = driver.switch_to.alert
#获取弹窗内容
print(alert.text)
#点击确定
alert.accept()
#点击取消
alert.dismiss()
'''
presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。
'''
#关闭浏览器 quit是关闭浏览器，close是关闭当前页
#driver.quit()