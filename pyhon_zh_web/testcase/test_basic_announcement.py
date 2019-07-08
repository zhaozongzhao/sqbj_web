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

    #创建公告(紧急通知)
    def test_creadeannouncement1(self):
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba = Basic(self.driver)
        page_basic_open(self.driver)
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.cread_announcement('自动创建的标题名称1','紧急通知','自动创建的内容',coverpicture,contentpicture)


    #创建公告(小区宣传)
    def test_creadeannouncement2(self):
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba = Basic(self.driver)
        page_basic_open(self.driver)
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.cread_announcement('自动创建的标题名称2','小区宣传','自动创建的内容',coverpicture,contentpicture)


    #创建公告(温馨提示)
    def test_creadeannouncement3(self):
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba = Basic(self.driver)
        page_basic_open(self.driver)
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.cread_announcement('自动创建的标题名称3','温馨提示','自动创建的内容',coverpicture,contentpicture)


    #创建缤纷发布公告:
    def test_releaseannouncement1(self):
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba = Basic(self.driver)
        time.sleep(2)
        page_basic_open(self.driver)
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.release_announcement('自动发布公告验证1','小区活动','自动发布的内容测试/n/t 测试换行',coverpicture,contentpicture)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

