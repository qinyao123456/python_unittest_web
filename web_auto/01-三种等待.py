from selenium import webdriver
import time

driver= webdriver.Chrome()

driver.get("https://www.winxuan.com/")
time.sleep(2)
driver.find_element_by_name("keyword").clear()
driver.find_element_by_name("keyword").send_keys("故事会")
#通过class_name查找元素，class属性值有两个，是由空格隔开的，只能取一个
driver.find_element_by_class_name("master-search-btn").click()

#关闭浏览器 quit是关闭浏览器，close是关闭当前页
driver.quit()

'''
Xpath:
1、绝对路径--不推荐
2、相对路径：
// 表示从根路径下开始查找
* 任意元素
[] 表示筛选条件
@  表示基于属性来栓选，例如@id = "kw"
contains模糊查询
//input[contains(text(),"xxxx")]
'''

'''
三种等待：
1、强制等待time.sleep()：只能够单次生效，无法做有效的判断，会浪费大量的时间
2、隐式等待 driver.implicitly_wait(10)：对webdriver对象设置全局等待，每一次操作，如遇到页面加载，则默认进入隐式等待，如
遇元素无法找到，则进入隐式等待，优势：设置一次即可
劣势：必须等待页面加载完成才会进入到后续的操作，或者等待超时在进入后续的操作(webdriver存在，隐式等待就一直存在)
3、强制等待
WebDriverWait(driver,10,0.5).until(lambda el:find_element_by_name("keyword")，message="超时，没找到元素")

在10秒规定时间内，每0.5秒去找一次keyword元素，找到返回true,则进行下面的操作，如果没找到元素，会显示message信息

driver.find_element_by_name("keyword").send_keys("故事会")


优势：
专门用于对指定的某一个元素进行等待
劣势：
一次只能针对一个元素生效，且相对复杂

WebDriverWait(driver,10,0.5).until_not(lamda el:find_xxxx)
没有找到元素 就会执行后面的操作

当多个等待一同被调用时，系统的等待时间取决于最长的等待时间 
'''
from selenium.webdriver.support.wait import WebDriverWait    #引入显示等待