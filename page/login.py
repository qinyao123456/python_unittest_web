from basePage.base_page import Tools
from selenium import webdriver
from selenium.webdriver.common.by import By

#类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
#函数名一律小写，如有多个单词，用下划线隔开
#继承
class LoginPage(Tools):
    #页面地址
    url = 'https://passport.winxuan.com/signin'
    #页面元素
    userName = (By.NAME,'account')
    password = (By.NAME,'password')
    loginBtn = (By.ID,'login_btn')
    #页面流程 找到元素输入账号、密码、点击
    #用输入、用点击
    def login(self,user,password):
        self.open(self.url)
        self.implicitlyWaitFun()
        self.input(self.userName,user)
        self.input(self.password,password)
        self.on_click(self.loginBtn)



if __name__ == '__main__':
    #打开浏览器
    #打断点，点击小虫子
    driver = LoginPage(webdriver.Chrome())
    driver.login('18349246200','qy123456')
