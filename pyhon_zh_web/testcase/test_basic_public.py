import unittest,time
from Action.basic_announcementlist import *
from Action.page_home import *
from Action.login import *
from Util.Excel import *
from Util.var import *
from Util.special import *

class test_basic(unittest.TestCase):

    def successful(self):
        Ba = Basic(self.driver)
        time.sleep(3)
        page_basic_open(self.driver)
        return Ba

    def setUp(self):
        info('##############################服务公示测试开始###############################')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.get('http://smart.sit2.sqbj.com/portal/login')
        self.pe = parseExcel(Excelobject_path)
        # self.alert = special(self.driver)
        login(self.driver,'18301565568','111111')
        self.Ba = self.successful()




    #创建公示(资质公示)
    def test_creadepublic1(self):
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        self.Ba.create_public('自动创建资质公示1','赵宗召','资质公示','自动创建的内容',coverpicture,contentpicture,'新建资质公示')
        assert '自动创建资质公示1' in self.Ba.select_table_publicelement(1,1,1).text

    #创建公示(物业服务)
    def test_creadepublic2(self):
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        self.Ba.create_public('自动创建物业服务1','赵宗召','物业服务','自动创建的内容',coverpicture,contentpicture,'物业服务')
        assert '自动创建物业服务1' in self.Ba.select_table_publicelement(1,1,1).text

    #创建公示(收费标准)
    def test_creadepublic3(self):
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        self.Ba.create_public('自动创建收费标准1','赵宗召','收费标准','自动创建的内容',coverpicture,contentpicture,'收费标准')
        assert '自动创建收费标准1' in self.Ba.select_table_publicelement(1,1,1).text

    #创建公示(设置运行公示)
    def test_creadepublic4(self):
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        self.Ba.create_public('自动创建设置运行公示1','赵宗召','设备运行公示','自动创建的内容',coverpicture,contentpicture,'设置运行公示')
        assert '自动创建设置运行公示1' in self.Ba.select_table_publicelement(1,1,1).text


    #发布服务公示
    def test_release_public1(self):
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        self.Ba.release_public('发布公示1','赵宗召','设备运行公示','自动创建的内容',coverpicture,contentpicture)
        assert '发布公示1' in self.Ba.select_table_publicelement(1,1,1).text

     #发布服务公示
    def test_release_public2(self):
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        self.Ba.release_public('发布资质公示1','赵宗召','资质公示','自动创建的内容',coverpicture,contentpicture)
        assert '发布资质公示1' in self.Ba.select_table_publicelement(1,1,1).text

     #发布服务公示
    def test_release_public3(self):
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        self.Ba.release_public('发布物业服务1','赵宗召','物业服务','自动创建的内容',coverpicture,contentpicture)
        assert '发布物业服务1' in self.Ba.select_table_publicelement(1,1,1).text

     #发布服务公示
    def test_release_public4(self):
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        self.Ba.release_public('发布收费标准1','赵宗召','收费标准','自动创建的内容',coverpicture,contentpicture)
        assert '发布收费标准1' in self.Ba.select_table_publicelement(1,1,1).text


    #删除服务公示
    def test_delete_public1(self):
        # Ba = self.successful()
        self.Ba.Enter_the_public()
        time.sleep(5)
        element = self.Ba.select_table_publicelement(1,1,1).text
        self.Ba.click_delete_button(1,6,'取消')
        assert element in self.Ba.select_table_publicelement(1,1,1).text

     #删除服务公示
    def test_delete_public2(self):
        # Ba = self.successful()
        self.Ba.Enter_the_public()
        element = self.Ba.select_table_publicelement(1,1,1).text
        self.Ba.click_delete_button(1,6,'确定')
        assert element not in self.Ba.select_table_publicelement(1,1,1).text



    def tearDown(self):
        info('##############################服务公示测试结束#######################################')
        self.driver.close()
        self.driver.quit()
