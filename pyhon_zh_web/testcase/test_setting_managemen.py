import unittest
from selenium import webdriver
from Action.login import *
from Action.page_home import *
from Action.charge_operation import *
from Util.Excel import *
from Util.var import *
from Util.special import *
class Test_login(unittest.TestCase):


    def setUp(self):
        self.driver =  webdriver.Chrome()
        self.driver.get('http://smart.sit2.sqbj.com/login')
        self.pe = parseExcel(Excelobject_path)
        self.alert = special(self.driver)
        login(self.driver,self.pe.get_cell_content(2,2),self.pe.get_cell_content(2,3))



    def tearDown(self):
        self.driver.close()

    #打开系统设置验证
    def test_open_charge(self):
        CH = Charge(self.driver)
        page_charge_open(self.driver)
        self.assertEqual('系统设置',CH.get_charge_setting_value())


    #添加收费管理员验证
    def test_add_charge_managemen(self):
         CH = Charge(self.driver)
         page_charge_open(self.driver)
         CH.add_charge_managemen('小区2号','收费员1')
         list = CH.get_list()
         self.assertIn('收费员1',list)


    #添加收费员验证
    def test_add_charge_choose(self):
         CH = Charge(self.driver)
         page_charge_open(self.driver)
         CH.add_charge_choose()
         time.sleep(2)
         list = CH.get_list()
         self.assertIn('小赵1',list)

    #设置收费管理员设置小区收费标准
    def test_set_charge_yes(self):
         CH = Charge(self.driver)
         page_charge_open(self.driver)
         CH.set_charge_permissions_yes()



    #禁止收费管理员设置小区收费标准
    def test_set_charge_no(self):
         CH = Charge(self.driver)
         page_charge_open(self.driver)
         CH.set_charge_permissions_no()






