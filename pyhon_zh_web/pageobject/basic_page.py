
import time
from Util.ParsePageObjectRepository import *
from Util.var import *
from Util.ObjectMap import *


class BasicPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.paser_page_object = ParsePageObjectRepository('BasicserverRepository.ini')
        self.basic_announcement = self.paser_page_object.getItemSection('Basic_announcement_home')
        print('验证返回信息',self.basic_announcement['announcement.page.communitynotice'].split('>'))
        self.wait = WebDriverWait(self.driver,10,0.5)

    #小区信息管理
    def Getannouncement_page(self):
        locateType, locateExpression = self.basic_announcement['announcement.page'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span

     #小区公告列表
    def Getannouncement_list(self):
        locateType, locateExpression = self.basic_announcement['announcement.list'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span

     #筛选标签状态
    def getannouncement_page(self):
        locateType, locateExpression = self.basic_announcement['announcement.page'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span

     #筛选标签状态:温馨提示
    def getannouncement_page_Lableprompt(self):

        locateType, locateExpression = self.basic_announcement['Lableprompt1'].split('>')
        print('验证信息',locateType,locateExpression)
        span = getElement(self.driver,locateType,locateExpression)
        return span

     #筛选标签状态:紧急通知
    def getannouncement_page_communitynotice(self):
        locateType, locateExpression = self.basic_announcement['announcement.page.communitynotice'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span
     #筛选标签状态:小区宣传
    def getannouncement_page_communitypropaganda(self):
        locateType, locateExpression = self.basic_announcement['announcement.page.communitypropaganda'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span

    #返回定位小区按钮
    def Add_anouncement_button(self):
        locateType, locateExpression = self.basic_announcement['add_announcement_button'].split('>')
        addbutton= getElement(self.driver,locateType,locateExpression)
        return addbutton

    #定位标题
    def add_announcement_inputlable(self):
        locateType, locateExpression = self.basic_announcement['add_announcement_inputlable'].split('>')
        Loadlbutton= getElement(self.driver,locateType,locateExpression)
        return Loadlbutton

    #定位内容输入框
    def add_announcement_div(self):
        locateType, locateExpression = self.basic_announcement['add_announcement_div'].split('>')
        Loadlbutton= getElement(self.driver,locateType,locateExpression)
        return Loadlbutton

    #定位保存按钮
    def save_announcement(self):
        locateType, locateExpression = self.basic_announcement['save_announcement'].split('>')
        Loadlbutton= getElement(self.driver,locateType,locateExpression)
        return Loadlbutton

    #定位标签
    def set_lable_announcement(self):
        locateType, locateExpression = self.basic_announcement['set_lable_announcement'].split('>')
        Loadlbutton= getElement(self.driver,locateType,locateExpression)
        return Loadlbutton