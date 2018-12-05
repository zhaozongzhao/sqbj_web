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

    #添加收费员
    def add_charge_choose(self):
        CH =  Charge_Page(self.driver)
        time.sleep(1)
        CH.open_setting().click()
        time.sleep(1)
        CH.charge_management().click()
        time.sleep(1)
        CH.charge_managenment_choose().click()
        time.sleep(1)
        CH.charge_community_select('赵哥小区二号').click()
        time.sleep(1)
        CH.charge_add_button().click()
        time.sleep(1)
        CH.charge_select_department().click()
        time.sleep(1)
        CH.charge_choose_inputs().click()
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



