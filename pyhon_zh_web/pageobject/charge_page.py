from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import traceback
from Util.ParsePageObjectRepository import *
from Util.var import *
from Util.ObjectMap import *
from selenium.webdriver.support.ui import Select

class Charge_Page(object):

    def __init__(self,driver):
        self.driver = driver
        self.paser_page_object = ParsePageObjectRepository()
        self.login_iteim = self.paser_page_object.getItemSection('zh_charge_page')
        self.wait = WebDriverWait(self.driver,10,0.2)

    #系统设置
    def open_setting(self):
         locateType, locateExpression = self.login_iteim['charge_setting'].split('>')
         setting = getElement(self.driver,locateType,locateExpression)
         return setting

    def open_setting_value(self):
         locateType, locateExpression = self.login_iteim['charge_setting'].split('>')
         setting = getElement(self.driver,locateType,locateExpression)
         return setting.text

    #收费人员管理
    def charge_management(self):
        locateType, locateExpression = self.login_iteim['charge_management'].split('>')
        setting = getElement(self.driver,locateType,locateExpression)
        return setting

    #费管理员设置
    def charge_management_add(self):
        locateType, locateExpression = self.login_iteim['charge_management_add'].split('>')
        managementsetting = getElement(self.driver,locateType,locateExpression)
        return managementsetting

    #收费员设置
    def charge_managenment_choose(self):
        locateType, locateExpression = self.login_iteim['charge_managenment_choose'].split('>')
        managementsetting = getElement(self.driver,locateType,locateExpression)
        return managementsetting

    #管理员权限设置
    def charge_management_permissions(self):
        locateType, locateExpression = self.login_iteim['charge_management_permissions'].split('>')
        permissions = getElement(self.driver,locateType,locateExpression)
        return permissions




    #选择择小区(收费管理员)
    def charge_community_select(self,selectcommunity):
          for i in range(4):
           locateType, locateExpression = self.login_iteim['charge_community_select'+str(i+1)].split('>')
           selectcommunityname = getElement(self.driver,locateType,locateExpression)
           if selectcommunityname.text == selectcommunity:
                  return selectcommunityname


    #添加按钮
    def charge_add_button(self):
        locateType, locateExpression = self.login_iteim['charge_add_button'].split('>')
        addbutton = getElement(self.driver,locateType,locateExpression)
        return addbutton

    #选择分组
    def charge_select_department(self):
        locateType, locateExpression = self.login_iteim['charge_select_department'].split('>')
        addbutton = getElement(self.driver,locateType,locateExpression)
        return addbutton

    #定位员工
    def charge_choose_inputs(self,employees):
        locateType, locateExpression = self.login_iteim['charge_choose_inputs'].split('>')
        locateExpression1 = locateExpression.replace('应用管理员',employees)
        addbutton = getElement(self.driver,locateType,locateExpression1)
        return addbutton

    #确定按钮
    def charge_button(self):
        locateType, locateExpression = self.login_iteim['charge_button'].split('>')
        addbutton = getElement(self.driver,locateType,locateExpression)
        return addbutton

    #定位列表
    def charge_management_table(self):
        locateType, locateExpression = self.login_iteim['table'].split('>')
        table = getElement(self.driver,locateType,locateExpression)
        return table

    #定位行
    def tr_table_list(self):
        table = self.charge_management_table()
        rows = table.find_elements_by_tag_name('tr')
        return rows

    #获取总列数
    def td_table_list(self,row):
        rows = row.find_elements_by_tag_name('td')
        return rows

    #设置收费员收费标准权限
    def charge_button_yes(self):
        locateType, locateExpression = self.login_iteim['charge_button_yes'].split('>')
        addbutton = getElement(self.driver,locateType,locateExpression)
        return addbutton

    #设置收费员收费标准权限
    def charge_button_no(self):
        locateType, locateExpression = self.login_iteim['charge_button_no'].split('>')
        addbutton = getElement(self.driver,locateType,locateExpression)
        return addbutton

    #修改封账退款权限
    def charge_administrator_permissions(self,employees):
        locateType, locateExpression = self.login_iteim['charge_administrator_permissions'].split('>')
        locateExpression1 = locateExpression.replace('应用管理员',employees)
        addbutton = getElement(self.driver,locateType,locateExpression1)
        return addbutton

    #点击可退按钮
    def charge_permissions_yes(self):
        locateType, locateExpression = self.login_iteim['charge_permissions_yes'].split('>')
        addbutton = getElement(self.driver,locateType,locateExpression)
        return addbutton

    #点击不可退按钮
    def charge_permissions_no(self):
        locateType, locateExpression = self.login_iteim['charge_permissions_no'].split('>')
        addbutton = getElement(self.driver,locateType,locateExpression)
        return addbutton

    #点击确定按钮
    def charge_determine_button(self):
        locateType, locateExpression = self.login_iteim['charge_permissions_determinebutton'].split('>')
        addbutton = getElement(self.driver,locateType,locateExpression)
        return addbutton