
from selenium import webdriver
from basePage.base_page import Tools
from selenium.webdriver.common.by import By

class Register(Tools):
    url = 'https://passport.winxuan.com/front/register/signup'
    #找元素
    mobile = (By.NAME,'mobile')
    code = (By.NAME, 'code')
    m_code = (By.NAME, 'm-code')
