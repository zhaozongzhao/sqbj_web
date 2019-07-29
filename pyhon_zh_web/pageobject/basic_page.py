
import time
from Util.ParsePageObjectRepository import *
from Util.var import *
from Util.ObjectMap import *
from selenium.webdriver.support import expected_conditions as EC
from Util.Table import Table


class Basic_announcement_Page(object):
    '''
    小区公告列表

    '''

    def __init__(self,driver):
        self.driver = driver
        self.paser_page_object = ParsePageObjectRepository('BasicserverRepository.ini')
        self.basic_announcement = self.paser_page_object.getItemSection('Basic_announcement_home')
        # info('返回配置的元素定位信息{}'.format(self.basic_announcement))
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
        h =  self.basic_announcement['lableprompt1']
        print(h)
        locateType, locateExpression = h.split('>')
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

     #筛选标签状态:小区活动
    def getannouncement_page_communityactivity(self):
        locateType, locateExpression = self.basic_announcement['announcement.page.communityactivity'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span

    #点击新建公告按钮
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
        # 创建一个显示等待
        wait = WebDriverWait(self.driver, 5, 0.5)
        # 判断被测上传按钮是否处于克点击状态
        wait.until(EC.element_to_be_clickable((locateType,locateExpression)))
        return Loadlbutton

    #定位发布按钮
    def release_announcement(self):
        locateType, locateExpression = self.basic_announcement['release_announcement'].split('>')
        Loadlbutton= getElement(self.driver,locateType,locateExpression)
        # 创建一个显示等待
        wait = WebDriverWait(self.driver, 5, 0.5)
        # 判断被测上传按钮是否处于克点击状态
        wait.until(EC.element_to_be_clickable((locateType,locateExpression)))
        return Loadlbutton

    #定位标签
    def set_lable_announcement(self):
        locateType, locateExpression = self.basic_announcement['set_lable_announcement'].split('>')
        Loadlbutton= getElement(self.driver,locateType,locateExpression)
        return Loadlbutton

    #封面图片
    def add_cover_picture(self):
        locateType, locateExpression = self.basic_announcement['add_announcement_inputcover'].split('>')
        Loadlbutton= getElements(self.driver,locateType,locateExpression)
        return Loadlbutton[0]

    #添加内容图片
    def add_content_picture(self):
        locateType, locateExpression = self.basic_announcement['add_announcement_inputcover'].split('>')
        Loadlbutton= getElements(self.driver,locateType,locateExpression)
        return Loadlbutton[2]

    #获取列表内容
    def get_table_announcement(self):
          locateType, locateExpression = self.basic_announcement['announcement_table'].split('>')
          Loadlbutton= getElement(self.driver,locateType,locateExpression)
          return Loadlbutton

#服务公示
class Basic_public_Page(object):
     '''
     服务公示列表

      '''


     #获取配置文件中的元素定位信息
     def __init__(self,driver):
        self.driver = driver
        self.paser_page_object = ParsePageObjectRepository('BasicserverRepository.ini')
        self.basic_announcement = self.paser_page_object.getItemSection('Basic_Of_the_public')
        info('返回配置的元素定位信息{}'.format(self.basic_announcement))
        self.wait = WebDriverWait(self.driver,10,0.5)




     #小区信息管理
     def Get_public_page(self):
        locateType, locateExpression = self.basic_announcement['public.page'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span


     #服务公示列表
     def getpublic_list(self):
        locateType, locateExpression = self.basic_announcement['public.list'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span

     #筛选标签状态:资质公示
     def getpublic_Lableprompt1(self):
        locateType, locateExpression = self.basic_announcement['public_Lableprompt1'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span


     #筛选标签状态:物业服务
     def getpublic_page_ommunitynotice(self):
        locateType, locateExpression = self.basic_announcement['public.page.communitynotice'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span

     #筛选标签状态:收费标准
     def getpublic_page_communitypropaganda(self):
        locateType, locateExpression = self.basic_announcement['public.page.communitypropaganda'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span

     #筛选标签状态:设备运行公示
     def getpublic_page_communityactivity(self):
        locateType, locateExpression = self.basic_announcement['public.page.communityactivity'].split('>')
        span = getElement(self.driver,locateType,locateExpression)
        return span

     #服务公示添加按钮
     def getadd_public_button(self):
         locateType,locateExpression = self.basic_announcement['add_public_button'].split('>')
         button = getElement(self.driver,locateType,locateExpression)
         return button

     #添加标题
     def add_public_inputlable(self):
         locateType,locateExpression = self.basic_announcement['add_public_inputlable'].split('>')
         button = getElement(self.driver,locateType,locateExpression)
         return button

     #添加发布人
     def  add_public_inputissuer(self):
          locateType,locateExpression = self.basic_announcement['add_public_inputissuer'].split('>')
          button = getElement(self.driver,locateType,locateExpression)
          return button


     #定位标签选择
     def set_lable_public(self):
          locateType,locateExpression = self.basic_announcement['set_lable_public'].split('>')
          button = getElement(self.driver,locateType,locateExpression)
          return button

     #定位服务标签按钮
     #资质公示
     def public_Lableprompt1(self):
          locateType,locateExpression = self.basic_announcement['public_lableprompt1'].split('>')
          button = getElement(self.driver,locateType,locateExpression)
          return button
     #物业服务
     def public_page_communitynotice(self):
         locateType,locateExpression = self.basic_announcement['public.page.communitynotice'].split('>')
         button = getElement(self.driver,locateType,locateExpression)
         return button
     #收费标准
     def public_page_communitypropaganda(self):
         locateType,locateExpression = self.basic_announcement['public.page.communitypropaganda'].split('>')
         button = getElement(self.driver,locateType,locateExpression)
         return button
     #设备运行公示
     def public_page_communityactivity(self):
          locateType,locateExpression = self.basic_announcement['public.page.communityactivity'].split('>')
          button = getElement(self.driver,locateType,locateExpression)
          return button

      #封面图片
     def add_cover_piblicpicture(self):
        locateType, locateExpression = self.basic_announcement['add_public_inputcover'].split('>')
        Loadlbutton= getElements(self.driver,locateType,locateExpression)
        return Loadlbutton[0]

     #添加内容图片
     def add_content_publicpicture(self):
        locateType, locateExpression = self.basic_announcement['add_public_inputcover'].split('>')
        Loadlbutton= getElements(self.driver,locateType,locateExpression)
        return Loadlbutton[2]
     #添加内容
     def add_public_div(self):
         locateType, locateExpression = self.basic_announcement['add_public_div'].split('>')
         Loadlbutton= getElement(self.driver,locateType,locateExpression)
         return Loadlbutton


     #获取列表内容
     def get_public_table(self):
          locateType, locateExpression = self.basic_announcement['public_table'].split('>')
          Loadlbutton= getElement(self.driver,locateType,locateExpression)
          return Loadlbutton



     #定位发布按钮
     def release_public(self):
        locateType, locateExpression = self.basic_announcement['release_public'].split('>')
        Loadlbutton= getElement(self.driver,locateType,locateExpression)
        # 创建一个显示等待
        wait = WebDriverWait(self.driver, 5, 0.5)
        # 判断被测上传按钮是否处于克点击状态
        wait.until(EC.element_to_be_clickable((locateType,locateExpression)))
        return Loadlbutton

     #点击预览按钮
     def Preview_button(self):
         locateType, locateExpression = self.basic_announcement['preview_button'].split('>')
         Loadlbutton= getElement(self.driver,locateType,locateExpression)
         # 创建一个显示等待
         wait = WebDriverWait(self.driver, 5, 0.5)
         # 判断被测上传按钮是否处于克点击状态
         wait.until(EC.element_to_be_clickable((locateType,locateExpression)))
         return Loadlbutton

     #关闭预览界面
     def close_Preview_button(self):
         locateType, locateExpression = self.basic_announcement['close_preview_button'].split('>')
         Loadlbutton= getElement(self.driver,locateType,locateExpression)
         # 创建一个显示等待
         wait = WebDriverWait(self.driver, 5, 0.5)
         # 判断被测上传按钮是否处于克点击状态
         wait.until(EC.element_to_be_clickable((locateType,locateExpression)))
         return Loadlbutton

     #点击保存按钮
     def create_save_public(self):
         locateType, locateExpression = self.basic_announcement['create_save_public'].split('>')
         Loadlbutton= getElement(self.driver,locateType,locateExpression)
         # 创建一个显示等待
         wait = WebDriverWait(self.driver, 5, 0.5)
         # 判断被测上传按钮是否处于克点击状态
         wait.until(EC.element_to_be_clickable((locateType,locateExpression)))
         return Loadlbutton

     #获取表格输入框的元素
     def  delete_table_element(self,tr,td):
         info("输入的测试数据:  第{}行   第{}列  ".format(tr,td))
         BSpage = Basic_public_Page(self.driver)
         webtable= Table(BSpage.get_public_table())
         button = webtable.getWebElementInCell(tr,td,'xpath',"//a[contains(text(),'删除')]")
         return button

     #点击弹出提示页面上的确认按钮
     def button_delete_determine(self):
         info('选择确认')
         locateType, locateExpression = self.basic_announcement['determine_button'].split('>')
         Loadlbutton= getElement(self.driver,locateType,locateExpression)
         return Loadlbutton

     #点击弹出提示页面上的取消按钮
     def button_delete_cancel(self):
         info('选择取消')
         locateType, locateExpression = self.basic_announcement['cancel_button'].split('>')
         Loadlbutton= getElement(self.driver,locateType,locateExpression)
         return Loadlbutton


     '''
     列表页筛选功能
     '''
     #返回列表页标签筛选框
     def slect_lable_public(self):
         locateType, locateExpression = self.basic_announcement['slect_lable_public'].split('>')
         divseleinput= getElement(self.driver,locateType,locateExpression)
         return divseleinput

     #定位标签选项(资质公示)
     def selectpublic_Lableprompt1(self):
         locateType, locateExpression = self.basic_announcement['selectpublic_Lableprompt1'].split('>')
         divseleinput= getElement(self.driver,locateType,locateExpression)
         return divseleinput


       #定位标签选项(物业服务)
     def selectpublic_page_communitynotice(self):
         locateType, locateExpression = self.basic_announcement['selectpublic_page_communitynotice'].split('>')
         divseleinput= getElement(self.driver,locateType,locateExpression)
         return divseleinput

      #定位标签选项(收费标准)
     def selectpublic_page_communitypropaganda(self):
         locateType, locateExpression = self.basic_announcement['selectpublic_page_communitypropaganda'].split('>')
         divseleinput= getElement(self.driver,locateType,locateExpression)
         return divseleinput


     #定位标签选项(收费标准)
     def selectpublic_page_communityactivity(self):
         locateType, locateExpression = self.basic_announcement['selectpublic_page_communityactivity'].split('>')
         divseleinput= getElement(self.driver,locateType,locateExpression)
         return divseleinput


     #定位筛选状态按钮(未发布)
     def selectpublic_type1_loable(self):
         locateType, locateExpression = self.basic_announcement['selectpublic_type1_loable'].split('>')
         divseleinput= getElement(self.driver,locateType,locateExpression)
         return divseleinput

     #定位筛选状态按钮(已发布)
     def selectpublic_type2_loable(self):
         locateType, locateExpression = self.basic_announcement['selectpublic_type2_loable'].split('>')
         divseleinput= getElement(self.driver,locateType,locateExpression)
         return divseleinput


     #定位筛选状态按钮(已删除)
     def selectpublic_type2_loable(self):
         locateType, locateExpression = self.basic_announcement['selectpublic_type3_loable'].split('>')
         divseleinput= getElement(self.driver,locateType,locateExpression)
         return divseleinput












