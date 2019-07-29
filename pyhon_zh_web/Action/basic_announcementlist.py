from pageobject.basic_page import *
from Action.page_home import *
from testcase.log import *
import traceback
from Action.login import *
from Util.Table import Table
from Util.special import *



class Basic:

    def __init__(self,driver):
        self.driver =  driver
    #################################小区公告##########################################

    #新建公告(保存不发布)
    def cread_announcement(self,title,label,content,coverpicture,contentpicture):
       try:
           info("输入的测试数据:  标题{}   标签{}  内容{}".format(title,label,content,coverpicture,contentpicture))
           BSpage = Basic_announcement_Page(self.driver)
           BSpage.Getannouncement_page().click()
           time.sleep(0.5)
           BSpage.Getannouncement_list().click()
           BSpage.Add_anouncement_button().click()
           BSpage.add_announcement_inputlable().send_keys(title)
           BSpage.set_lable_announcement().click()
           if label == '紧急通知':
              BSpage.getannouncement_page_communitynotice().click()
              time.sleep(1)
           elif label == '小区宣传':
              BSpage.getannouncement_page_communitypropaganda().click()
           elif label == "温馨提示":
              BSpage.getannouncement_page_Lableprompt().click()
           BSpage.add_cover_picture().send_keys(coverpicture)
           BSpage.add_announcement_div().send_keys(content)
           BSpage.add_content_picture().send_keys(contentpicture)

           BSpage.save_announcement().click()
           info('创建完成任务{}'.format(title))
       except Exception  as ERROR:
           debug('创建公告错误{}'.format(ERROR))
           traceback.print_exc(ERROR)

    #创建并发布公告
    def release_announcement(self,title,label,content,coverpicture,contentpicture):
       try:
           info("输入的测试数据:  标题{}   标签{}  内容{}".format(title,label,content,coverpicture,contentpicture))
           BSpage = Basic_announcement_Page(self.driver)
           BSpage.Getannouncement_page().click()
           time.sleep(0.5)
           BSpage.Getannouncement_list().click()
           BSpage.Add_anouncement_button().click()
           BSpage.add_announcement_inputlable().send_keys(title)
           BSpage.set_lable_announcement().click()
           if label == '紧急通知':
              BSpage.getannouncement_page_communitynotice().click()
              time.sleep(1)
           elif label == '小区宣传':
              BSpage.getannouncement_page_communitypropaganda().click()
           elif label == "温馨提示":
              BSpage.getannouncement_page_Lableprompt().click()
           BSpage.add_cover_picture().send_keys(coverpicture)
           BSpage.add_announcement_div().send_keys(content)
           BSpage.add_content_picture().send_keys(contentpicture)
           #发布公告
           time.sleep(3)
           BSpage.release_announcement().click()
           info('创建完成任务{}'.format(title))
       except Exception  as ERROR:
           debug('创建公告错误{}'.format(ERROR))
           traceback.print_exc(ERROR)

    #验证table中的内容
    def  select_table_element(self,tr,td,celltext=0):
         info("输入的测试数据:  第{}行   第{}列  内容{}".format(tr,td,celltext))
         BSpage = Basic_announcement_Page(self.driver)
         BSpage.Getannouncement_page().click()
         time.sleep(2)
         BSpage.Getannouncement_list().click()
         time.sleep(2)
         webtable= Table(BSpage.get_table_announcement())
         # webtable = table()
         if celltext == '行数':
             return webtable.getRowCount()
         elif celltext == '列数':
             return  webtable.getColumnCount()
         else:
             return  webtable.getCell(tr,td)

    #    #删除服务公示
    # def click_delete_button(self,tr,td,choose):
    #      BSpage = Basic_public_Page(self.driver)
    #      BSpage.Get_public_page().click()
    #      time.sleep(0.5)
    #      BSpage.getpublic_list().click()
    #      time.sleep(0.5)
    #      deletebutton =  BSpage.delete_table_element(tr,td)
    #      deletebutton.click()
    #      time.sleep(0.5)
    #      if choose == '取消':
    #          BSpage.button_delete_cancel()
    #      elif choose == '确定':
    #          BSpage.button_delete_determine().click()


    #######################################服务公示####################################

    #进入服务公示界面
    def Enter_the_public(self):
          BSpage = Basic_public_Page(self.driver)
          BSpage.Get_public_page().click()
          time.sleep(0.5)
          BSpage.getpublic_list().click()
          time.sleep(0.5)
          return  BSpage




    #创建发布服务公示
    def release_public(self,title,issuer,label,content,coverpicture,contentpicture):
       try:
           info("输入的测试数据:  标题{}   标签{}  内容{}".format(title,issuer,label,content,coverpicture,contentpicture))
           # BSpage = Basic_public_Page(self.driver)
           # BSpage.Get_public_page().click()
           # time.sleep(0.5)
           # BSpage.getpublic_list().click()
           # time.sleep(0.5)
           BSpage = self.Enter_the_public()
           BSpage.getadd_public_button().click()
           BSpage.add_public_inputlable().send_keys(title)
           BSpage.add_public_inputissuer().send_keys(issuer)
           BSpage.set_lable_public().click()
           if label == '资质公示':
              BSpage.public_Lableprompt1().click()
              time.sleep(1)
           elif label == '物业服务':
              BSpage.public_page_communitynotice().click()
           elif label == "收费标准":
              BSpage.public_page_communitypropaganda().click()
           elif label == '设备运行公示':
              BSpage.public_page_communityactivity().click()
           BSpage.add_cover_piblicpicture().send_keys(coverpicture)
           BSpage.add_public_div().send_keys(content)
           BSpage.add_content_publicpicture().send_keys(contentpicture)
           #发布公告
           time.sleep(3)
           BSpage.release_public().click()
           info('创建完成任务{}'.format(title))
       except Exception  as ERROR:
           debug('创建公告错误{}'.format(ERROR))
           traceback.print_exc(ERROR)

    #创建保存按钮
    def create_public(self,title,issuer,label,content,coverpicture,contentpicture,screenshots):
       try:
           info("输入的测试数据:  标题{}   标签{}  内容{}".format(title,issuer,label,content,coverpicture,contentpicture,screenshots))
           # BSpage = Basic_public_Page(self.driver)
           # BSpage.Get_public_page().click()
           # time.sleep(0.5)
           # BSpage.getpublic_list().click()
           # time.sleep(0.5)
           BSpage = self.Enter_the_public()
           BSpage.getadd_public_button().click()
           BSpage.add_public_inputlable().send_keys(title)
           BSpage.add_public_inputissuer().send_keys(issuer)
           BSpage.set_lable_public().click()
           if label == '资质公示':
              BSpage.public_Lableprompt1().click()
              time.sleep(1)
           elif label == '物业服务':
              BSpage.public_page_communitynotice().click()
           elif label == "收费标准":
              BSpage.public_page_communitypropaganda().click()
           elif label == '设备运行公示':
              BSpage.public_page_communityactivity().click()
           BSpage.add_cover_piblicpicture().send_keys(coverpicture)
           BSpage.add_public_div().send_keys(content)
           BSpage.add_content_publicpicture().send_keys(contentpicture)
           #发布公告
           time.sleep(2)
           BSpage.Preview_button().click()
           time.sleep(0.5)
           self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/'+screenshots+'.png')
           BSpage.close_Preview_button().click()
           time.sleep(2)
           BSpage.create_save_public().click()
           info('创建完成任务{}'.format(title))
       except Exception  as ERROR:
           debug('创建公告错误{}'.format(ERROR))
           traceback.print_exc(ERROR)



    # #删除服务公示
    def click_delete_button(self,tr,td,choose):
         '''
         根据传入的行号和列号,点击单元框中的元素

         '''
         BSpage = Basic_public_Page(self.driver)
         # BSpage.Get_public_page().click()
         # time.sleep(0.5)
         # BSpage.getpublic_list().click()
         # time.sleep(0.5)
         # BSpage = self.Enter_the_public()
         deletebutton =  BSpage.delete_table_element(tr,td)
         deletebutton.click()
         time.sleep(0.5)
         if choose == '取消':
             BSpage.button_delete_cancel()
         elif choose == '确定':
             BSpage.button_delete_determine().click()


    #获取服务公示页面table中指定单元格中的元素
     #验证table中的内容
    def  select_table_publicelement(self,tr,td,celltext=0):
         info("输入的测试数据:  第{}行   第{}列  是否打开也是0是1否".format(tr,td,celltext))
         # BSpage = Basic_announcement_Page(self.driver)
         # BSpage.Getannouncement_page().click()
         # time.sleep(2)
         # BSpage.Getannouncement_list().click()
         # time.sleep(2)
         if celltext ==0:
            BSpage = self.Enter_the_public()
         elif celltext ==1:
            BSpage = Basic_public_Page(self.driver)
         webtable= Table(BSpage.get_public_table())
         # webtable = table()
         return  webtable.getCell(tr,td)

    #获取最大行数
    def getRownumberCount(self):
        BSpage = Basic_public_Page(self.driver)
        webtable= Table(BSpage.get_public_table())
        return webtable.getRowCount()






if __name__ == '__main__':
    #测试代码
        driver = webdriver.Chrome()
        driver.get('http://smart.sit2.sqbj.com/portal/login')
        Ba = Basic(driver)
        login(driver,'18301565568','111111')
        time.sleep(3)
        page_basic_open(driver)
        Ba.Enter_the_public()
        # Ba.release_announcement('自动创建的标题名称3','温馨提示','自动创建的内容',
        #                       '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png','/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        # Ba.release_public('自动发布服务公示101','发布人','资质公示','自动发布的内容测试/n/t 测试换行','/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png','/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        # print(Ba.select_table_element(2,2,'行数'))
        # print(Ba.select_table_element(2,2,'列数'))
        # print(Ba.select_table_element(4,1,0).text)
        # Ba.create_public('自动发布设备运行公示','发布人','设备运行公示','自动发布的内容测试/n/t 测试换行','/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png','/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png','预览截图')
        # time.sleep(0.5)
        # element = Ba.select_table_publicelement(1,1,0)
        # # time.sleep(3)
        # Ba.click_delete_button(1,6,'取消')
        # assert  element == Ba.select_table_publicelement(1,1,1)
        # driver.close()

        print(Ba.getRownumberCount())