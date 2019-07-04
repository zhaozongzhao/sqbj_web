from  pageobject.Home_page import *

from selenium import webdriver

#进入物业收费
def page_charge_open(driver):
    HP = HomePage(driver)
    HP.open_charge().click()

#获取登用户名称
def get_name(driver):
    HP = HomePage(driver)
    time.sleep(2)
    name =  HP.get_login_name()
    time.sleep(1)
    return name

#进入基础服务
def page_basic_open(driver):
    HP = HomePage(driver)
    HP.open_basic().click()