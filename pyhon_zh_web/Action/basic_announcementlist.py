from pageobject.basic_page import *
from selenium import webdriver


#新建公告
def cread_announcement(driver,title,label,content):
     BSpage =  BasicPage(driver)
     BSpage.Getannouncement_page_communityselect().click()
     BSpage.Getannouncement_list().click()
     BSpage.Add_anouncement_button().click()
     BSpage.add_announcement_inputlable().send_keys('验证标题名称1')
     BSpage.set_lable_announcement().click()
     BSpage.getannouncement_page_Lableprompt().click()
     BSpage.add_announcement_div().send_keys('内定信息')
     BSpage.save_announcement().click()




# if __name__ == '__main__':
#     #测试代码
