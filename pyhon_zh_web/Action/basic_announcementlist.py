from pageobject.basic_page import *
from Action.page_home import *
from testcase.log import *
import traceback
from Action.login import *
from Util.Table import Table



class Basic:

    def __init__(self,driver):
        self.driver =  driver


    #新建公告(保存不发布)
    def cread_announcement(self,title,label,content,coverpicture,contentpicture):
       try:
           info("输入的测试数据:  标题{}   标签{}  内容{}".format(title,label,content,coverpicture,contentpicture))
           BSpage = BasicPage(self.driver)
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
           BSpage = BasicPage(self.driver)
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
         BSpage = BasicPage(self.driver)
         # BSpage.Getannouncement_page().click()
         # time.sleep(2)
         # BSpage.Getannouncement_list().click()
         # time.sleep(2)
         webtable= Table(BSpage.get_table_announcement())
         # webtable = table()
         if celltext == '行数':
             return webtable.getRowCount()
         elif celltext == '列数':
             return  webtable.getColumnCount()
         else:
             return  webtable.getCell(tr,td)




if __name__ == '__main__':
    #测试代码
        driver = webdriver.Chrome()
        driver.get('http://smart.sit2.sqbj.com/portal/login')
        Ba = Basic(driver)
        login(driver,'18301565568','111111')
        time.sleep(3)
        page_basic_open(driver)
        # Ba.release_announcement('自动创建的标题名称3','温馨提示','自动创建的内容',
        #                       '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png','/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba.release_announcement('自动发布公告验证1','小区活动','自动发布的内容测试/n/t 测试换行','/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png','/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        # print(Ba.select_table_element(2,2,'行数'))
        # print(Ba.select_table_element(2,2,'列数'))
        # print(Ba.select_table_element(4,1,0).text)

        # Ba.select_table_element(1,1,'列数')
        driver.quit()