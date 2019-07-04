from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import traceback
from Util.ParsePageObjectRepository import *
from Util.var import *
from Util.ObjectMap import *
from selenium.webdriver.support.ui import Select


class HomePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.paser_page_object = ParsePageObjectRepository('PageObjectRepository')
        self.login_iteim = self.paser_page_object.getItemSection('zh_page_home')
        self.wait = WebDriverWait(self.driver,10,0.2)

    #定位物业收费
    def open_charge(self):
        locateType, locateExpression = self.login_iteim['page.charge'].split('>')
        charge = getElement(self.driver,locateType,locateExpression)
        return charge

    #定位基础服务
    def open_basic(self):
        locateType, locateExpression = self.login_iteim['page.basic_services'].split('>')
        charge = getElement(self.driver,locateType,locateExpression)
        return charge


    def get_login_name(self):
        locateType, locateExpression = self.login_iteim['page.personal'].split('>')
        time.sleep(1)
        name = getElement(self.driver,locateType,locateExpression).text
        print(name)
        return name



