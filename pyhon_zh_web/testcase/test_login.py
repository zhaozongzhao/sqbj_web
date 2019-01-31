import unittest
from selenium import webdriver
from Action.login import *
from Action.page_home import *
from Util.Excel import *
from Util.var import *
from Util.special import *
class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome()
        self.driver.get('http://smart.sit2.sqbj.com/portal/login')
        self.pe = parseExcel(Excelobject_path)
        self.alert = special(self.driver)

    def tearDown(self):
        self.driver.close()

    #正确用户正确密码
    def test_login_true(self):
        login(self.driver,self.pe.get_cell_content(2,2),self.pe.get_cell_content(2,3))
        time.sleep(5)
        assert self.pe.get_cell_content(2,4) in self.driver.page_source



    #不同角色用户登录
    def test_login_role_true(self):
        login(self.driver,self.pe.get_cell_content(3,2),self.pe.get_cell_content(3,3))
        assert self.pe.get_cell_content(3,4) in self.driver.page_source


    #使用其他用户的密码登陆
    def test_login_passworderror(self):
        login(self.driver,self.pe.get_cell_content(4,2),self.pe.get_cell_content(4,3))
        time.sleep(3)
        print(geterror(self.driver))
        self.assertCountEqual(self.pe.get_cell_content(4,4),geterror(self.driver))

    #手机号码不存在
    def test_login_usererror(self):
        login(self.driver,self.pe.get_cell_content(5,2),self.pe.get_cell_content(5,3))
        time.sleep(3)
        print(geterror(self.driver))
        self.assertCountEqual(self.pe.get_cell_content(5,4),geterror(self.driver))

if __name__ == '__main__':
    Test_login()