import unittest
import ddt
from Action.login import *
from Action.page_home import *
from Util.Excel import *
from Util.special import *
from Util.var import *
from testcase.log import *

pe = parseExcel(Excelobject_path)
All_case_date = pe.get_caseDatas_all()
info(All_case_date)

@ddt.ddt
class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome()
        url ='http://smart.sit2.sqbj.com/portal/login'
        self.driver.get(url)
        info('##########################执行开始########################################')
        info('登陆地址{}'.format(url))
        self.alert = special(self.driver)

    def tearDown(self):
        info('###########################执行结束##########################################')
        self.driver.close()

    @ddt.data(*All_case_date)
    def test_login_true(self,case_data):
        try:

          info('登陆用户名{},密码{}'.format(case_data['username'],case_data['password']))
          login(self.driver,case_data['username'],case_data['password'])
          time.sleep(10)
          info('登陆校验信息{},{}'.format(case_data['matching'],case_data['assertuaser']))
          if case_data['matching'] ==0:
              time.sleep(3)
              assert case_data['assertuaser'] in self.driver.page_source
          elif case_data['matching'] ==1:
              self.assertEqual(case_data['assertuaser'],geterror(self.driver))
        except AssertionError as e:
              debug('校验数据{},预期{},失败'.format(case_data['assertuaser'],geterror(self.driver)))
        except Exception as e:
              traceback.print_exc(e)
              debug('未知错误{}'.format(e))
        else:
              info('校验数据{},预期{},通过'.format(case_data['assertuaser'],self.driver.page_source))


    #  #正确用户正确密码
    # def test_login_true(self):
    #     login(self.driver,self.pe.get_cell_content(2,2),self.pe.get_cell_content(2,3))
    #     time.sleep(5)
    #     assert self.pe.get_cell_content(2,4) in self.driver.page_source
    #

    # #不同角色用户登录
    # def test_login_role_true(self):
    #     login(self.driver,self.pe.get_cell_content(3,2),self.pe.get_cell_content(3,3))
    #     assert self.pe.get_cell_content(3,4) in self.driver.page_source
    #
    #
    # #使用其他用户的密码登陆
    # def test_login_passworderror(self):
    #     login(self.driver,self.pe.get_cell_content(4,2),self.pe.get_cell_content(4,3))
    #     time.sleep(3)
    #     print(geterror(self.driver))
    #     self.assertCountEqual(self.pe.get_cell_content(4,4),geterror(self.driver))
    #
    # #手机号码不存在
    # def test_login_usererror(self):
    #     login(self.driver,self.pe.get_cell_content(5,2),self.pe.get_cell_content(5,3))
    #     time.sleep(3)
    #     print(geterror(self.driver))
    #     self.assertCountEqual(self.pe.get_cell_content(5,4),geterror(self.driver))

#