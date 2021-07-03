from basePage.base_page import Tools
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ChoicePage(Tools):
    #页面内地址
    url = 'https://www.winxuan.com/'
    #页面元素
    keyword = (By.NAME,'keyword')
    search = (By.XPATH,"//button[@type='submit']")
    #页面流程
    def searchBook(self,txt):
        self.open(self.url)
        self.implicitlyWaitFun()
        self.clear(self.keyword)
        time.sleep(2)
        self.input(self.keyword,txt)
        self.on_click(self.search)

if __name__ == '__main__':
    driver = ChoicePage(webdriver.Chrome())
    driver.searchBook('你好,李焕英')
