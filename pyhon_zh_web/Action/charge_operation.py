from  pageobject.charge_page import *
import time

from selenium import webdriver

class Charge:

    def __init__(self,driver):
        self.driver =  driver


    #添加收费管理员
    def add_charge_managemen(self,community,employees):
        CH =  Charge_Page(self.driver)
        time.sleep(1)
        CH.open_setting().click()
        time.sleep(1)
        CH.charge_management().click()
        time.sleep(1)
        CH.charge_management_add().click()
        time.sleep(1)
        CH.charge_community_select(community).click()
        time.sleep(1)
        CH.charge_add_button().click()
        time.sleep(1)
        # CH.charge_select_department().click()
        time.sleep(1)
        CH.charge_choose_inputs(employees).click()
        time.sleep(1)
        CH.charge_button().click()
        time.sleep(1)
        #刷新浏览器
        self.driver.refresh()
        CH.charge_community_select(community).click()

    #添加收费员
    def add_charge_choose(self,community,employees):
        CH =  Charge_Page(self.driver)
        time.sleep(1)
        CH.open_setting().click()
        time.sleep(1)
        CH.charge_management().click()
        time.sleep(1)
        CH.charge_managenment_choose().click()
        time.sleep(1)
        CH.charge_community_select(community).click()
        time.sleep(1)
        CH.charge_add_button().click()
        time.sleep(1)
        # CH.charge_select_department().click()
        time.sleep(1)
        CH.charge_choose_inputs(employees).click()
        time.sleep(1)
        CH.charge_button().click()

    #设置系统管理员权限
    def set_charge_permissions_yes(self):
        CH =  Charge_Page(self.driver)
        time.sleep(1)
        CH.open_setting().click()
        time.sleep(1)
        CH.charge_management().click()
        time.sleep(1)
        CH.charge_management_permissions().click()
        time.sleep(0.5)
        if not CH.charge_button_yes().is_selected():
           CH.charge_button_yes().click()

    #禁止收费管理员设置小区收费标准
    def set_charge_permissions_no(self):
        CH =  Charge_Page(self.driver)
        time.sleep(1)
        CH.open_setting().click()
        time.sleep(1)
        CH.charge_management().click()
        time.sleep(1)
        CH.charge_management_permissions().click()
        time.sleep(3)
        if not CH.charge_button_no().is_selected():
           CH.charge_button_no().click()

    #获取系统设置菜单名称
    def get_charge_setting_value(self):
        CH =  Charge_Page(self.driver)
        return CH.open_setting_value()

    #获取收费管理员列表内容
    def get_list(self):
         time.sleep(1)
         list = []
         CH =  Charge_Page(self.driver)
         for i in CH.tr_table_list():
             for j in CH.td_table_list(i):
                  list.append(j.text)
         return list

    #设置退款权限
    def amend_administrator_permissions(self,community,employees,type):
       CH =  Charge_Page(self.driver)
       time.sleep(1)
       CH.open_setting().click()
       time.sleep(1)
       CH.charge_management().click()
       time.sleep(1)
       CH.charge_management_add().click()
       time.sleep(1)
       CH.charge_community_select(community).click()
       time.sleep(4)
       CH.charge_administrator_permissions(employees).click()
       time.sleep(0.5)
       if type ==1:
          if not CH.charge_permissions_yes().is_selected():
               CH.charge_permissions_yes().click()
       else:
          if not CH.charge_permissions_no().is_selected():
               CH.charge_permissions_no().click()
       time.sleep(0.5)
       CH.charge_determine_button1().click()


    #删除已经添加的员工
    def delete_employeelf(self,community,employees,):
       CH =Charge_Page(self.driver)
       time.sleep(1)
       CH.open_setting().click()
       time.sleep(1)
       CH.charge_management().click()
       time.sleep(1)
       CH.charge_management_add().click()
       time.sleep(1)
       CH.charge_community_select(community).click()
       time.sleep(3)
       CH.charge_delete_employees(employees).click()
       time.sleep(1)
       CH.charge_determine_button2().click()


