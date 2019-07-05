from pageobject.basic_page import *
from selenium import webdriver

class Basic:

    def __init__(self,driver):
        self.driver =  driver
   #新建公告
    def cread_announcement(self,title,label,content):
       BSpage =  BasicPage(self.driver)
       BSpage.Getannouncement_page().click()
       time.sleep(0.5)
       BSpage.Getannouncement_list().click()
       time.sleep(0.5)
       BSpage.Add_anouncement_button().click()
       time.sleep(0.5)
       BSpage.add_announcement_inputlable().send_keys('是是是')
       time.sleep(0.5)
       BSpage.set_lable_announcement().click()
       time.sleep(6)
       BSpage.getannouncement_page_communitynotice().click()
       time.sleep(1)
       BSpage.add_announcement_div().send_keys(content)
       time.sleep(1)
       BSpage.save_announcement().click()




# if __name__ == '__main__':
#     #测试代码
