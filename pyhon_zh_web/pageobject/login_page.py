from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import traceback
from Util.ParsePageObjectRepository import *
from Util.var import *
from Util.ObjectMap import *
from selenium.webdriver.support.ui import Select

class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.paser_page_object = ParsePageObjectRepository()
        self.login_iteim = self.paser_page_object.getItemSection('zh_login_page')
        print(self.login_iteim)
        self.wait = WebDriverWait(self.driver,10,0.2)

    # def getFrame(self):
    #     locateType,locateExpression =  self.login_iteim['login_page.frame'].split('>')
    #     print(locateType,locateExpression)
    #     frame = getElement(self.driver,locateType,locateExpression)
    #     return frame

    # def getclick(self):
    #     locateType, locateExpression = self.login_iteim['login_page.click'].split('>')
    #     print(locateType, locateExpression)
    #     click = getElement(self.driver,locateType,locateExpression)
    #     return click

    def getUserName(self):
        locateType, locateExpression = self.login_iteim['login_page.username'].split('>')
        usreName = getElement(self.driver,locateType,locateExpression)
        return usreName

    def getPassword(self):
        locateType, locateExpression = self.login_iteim['login_page.password'].split('>')
        password = getElement(self.driver,locateType,locateExpression)
        return password
    #选择框
    def getProjectinput(self):
        locateType,locateExpression = self.login_iteim['login_page.project'].split('>')
        options =  getElement(self.driver,locateType,locateExpression)
        return options
    #选择标识
    def getProjectvalue(self):
        locateType,locateExpression = self.login_iteim['login_page.options'].split('>')
        options =  getElement(self.driver,locateType,locateExpression)
        return options

    def getLoginButton(self):
        locateType,locateExpression = self.login_iteim['login_page.button1'].split('>')
        loginbutton = getElement(self.driver,locateType,locateExpression)
        return loginbutton

    def getuserorpassworderror(self):
        locateType,locateExpression = self.login_iteim['login_page.error'].split('>')
        time.sleep(1)
        loginbutton = getElement(self.driver,locateType,locateExpression)
        error = loginbutton.get_attribute('textContent')
        print(error)
        return error

