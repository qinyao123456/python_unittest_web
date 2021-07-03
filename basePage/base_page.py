#项目上常用的操作
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Tools:
    #初始化函数 浏览器(用后面的方法之前必须要初始化一个浏览器)
    def __init__(self,driver):
        self.driver = driver

    #访问
    def open(self,url):
        self.driver.get(url)
    #元素定位  *解包元组  (by.name,pwd)
    def locator(self,loc):
        return self.driver.find_element(*loc)
    #清除元素
    def clear(self,loc):
        self.locator(loc).clear()
    #输入  先要定位到，才能输入
    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)
    #回车
    def keys_enter(self,loc):
        self.locator(loc).send_keys(Keys.ENTER)
    #点击
    def on_click(self,loc):
        self.locator(loc).click()
    #强制等待
    def sleepWaitFun(self):
        time.sleep(3)
    #隐式等待
    def implicitlyWaitFun(self):
        self.driver.implicitly_wait(3)
    #显示等待
    def webDriverWaitFun(self):
        pass
    #关闭
    def quit(self):
        self.driver.quit()

