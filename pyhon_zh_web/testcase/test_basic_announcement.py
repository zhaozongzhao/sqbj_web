import unittest,time
from Action.basic_announcementlist import *
from Action.page_home import *
from Action.login import *
from Util.Excel import *
from Util.var import *
from Util.special import *

class test_basic(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.get('http://smart.sit2.sqbj.com/portal/login')
        self.pe = parseExcel(Excelobject_path)
        # self.alert = special(self.driver)
        login(self.driver,'18301565568','111111')

    #创建公告
    def test_creadeannouncement(self):
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba = Basic(self.driver)
        page_basic_open(self.driver)
        Ba.cread_announcement(self.driver,'自动创建的标题名称1','自动创建的内容')



    def tearDown(self):
        self.driver.close()

