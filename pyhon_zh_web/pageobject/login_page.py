
import time
from Util.ParsePageObjectRepository import *
from Util.var import *
from Util.ObjectMap import *


class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.paser_page_object = ParsePageObjectRepository('LoginPageRepository.ini')
        self.login_iteim = self.paser_page_object.getItemSection('zh_login_page')
        print(self.login_iteim)
        self.wait = WebDriverWait(self.driver,10,0.5)

    #定位用户名
    def getUserName(self):
        locateType, locateExpression = self.login_iteim['login_page.username'].split('>')
        usreName = getElement(self.driver,locateType,locateExpression)
        return usreName

    #定位密码
    def getPassword(self):
        locateType, locateExpression = self.login_iteim['login_page.password'].split('>')
        password = getElement(self.driver,locateType,locateExpression)
        return password
    #定位选择框
    def getProjectinput(self):
        locateType,locateExpression = self.login_iteim['login_page.project'].split('>')
        options =  getElement(self.driver,locateType,locateExpression)
        return options
    #选择租户--定位元素中通过contains()筛选元素
    def getProjectvalue(self):
        locateType,locateExpression = self.login_iteim['login_page.options'].split('>')
        options =  getElement(self.driver,locateType,locateExpression)
        return options

    #获取登陆按钮
    def getLoginButton(self):
        locateType,locateExpression = self.login_iteim['login_page.button1'].split('>')
        loginbutton = getElement(self.driver,locateType,locateExpression)
        return loginbutton

    #获取当前选择的租户信息
    def getuserorpassworderror(self):
        locateType,locateExpression = self.login_iteim['login_page.error'].split('>')
        time.sleep(1)
        loginbutton1 = getElement(self.driver,locateType,locateExpression)
        return tenant

    #判断存在租户
    def gettenant(self):
        liumber = self.driver.find_elements_by_xpath('//li[@role="option"]')
        return liumber

