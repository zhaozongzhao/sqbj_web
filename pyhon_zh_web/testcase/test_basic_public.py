import unittest
from Action.basic_announcementlist import *
from Action.page_home import *
from Action.login import *
from BeautifulReport import BeautifulReport
from Util.Excel import *
from Util.var import *






class test_basic1(unittest.TestCase):
    # 保存图片
    #
    def save_img(self, imf_name):
        """
         输入要保存的图片名称
        """
        self.driver.save_screenshot('{}/{}.png'.format(img_path, imf_name))



    def successful(self):
        Ba = Basic(self.driver)
        time.sleep(3)
        page_basic_open(self.driver)
        return Ba

    # def successful1(self,func):
    #     login(self.driver, '18301565568', '111111')
    #     def warpper(*args,**kwargs):
    #              Ba = Basic(self.driver)
    #              time.sleep(3)
    #              page_basic_open(self.driver)
    #              return Ba
    #     return  warpper



    def setUp(self):
        """
        打开无头浏览器,并进入基础服务页面

        """
        info('##############################服务公示测试开始###############################')
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.driver.get('http://smart.sit2.sqbj.com/portal/login')
        self.pe = parseExcel(Excelobject_path)
        login(self.driver, '18301565568', '111111')
        # self.alert = special(self.driver)

    @BeautifulReport.add_test_img('创建资质公示完成')
    def test_creadepublic1(self):
        '''
        创建公示(资质公示)
        '''
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba = self.successful()
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.create_public('自动创建资质公示1', '赵宗召',
                              '资质公示', '自动创建的内容',
                              # 上传的文件地址
                              coverpicture, contentpicture,
                              '新建资质公示')
        self.save_img('创建资质公示完成')
        assert '自动创建资质公示1' in Ba.select_table_publicelement(1, 1, 1).text

    @BeautifulReport.add_test_img(' 创建公示(物业服务)')
    def test_creadepublic2(self):
        '''
         创建公示(物业服务)
        '''
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba = self.successful()
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.create_public('自动创建物业服务1', '赵宗召', '物业服务', '自动创建的内容', coverpicture, contentpicture, '物业服务')
        self.save_img('创建公示(物业服务)')
        assert '自动创建物业服务1' in Ba.select_table_publicelement(1, 1, 1).text

    @BeautifulReport.add_test_img('创建公示(收费标准)')
    def test_creadepublic3(self):
        '''c
        # 创建公示(收费标准)
        '''
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba = self.successful()
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.create_public('自动创建收费标准1', '赵宗召', '收费标准', '自动创建的内容', coverpicture, contentpicture, '收费标准')
        self.save_img('创建公示(收费标准)')
        assert '自动创建收费标准1' in Ba.select_table_publicelement(1, 1, 1).text

    def test_creadepublic4(self):
        '''
        创建公示(设置运行公示)
        '''
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png')
        Ba = self.successful()
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.create_public('自动创建设置运行公示1', '赵宗召', '设备运行公示', '自动创建的内容', coverpicture, contentpicture, '设置运行公示')
        assert '自动创建设置运行公示1' in Ba.select_table_publicelement(1, 1, 1).text

    # 发布服务公示
    def test_release_public1(self):
        '''
        发布服务公示
        '''
        Ba = self.successful()
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.release_public('发布公示1', '赵宗召', '设备运行公示', '自动创建的内容', coverpicture, contentpicture)
        assert '发布公示1' in Ba.select_table_publicelement(1, 1, 1).text

        # 发布服务公示

    def test_release_public2(self):
        '''
        发布服务公示
        '''
        Ba = self.successful()
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.release_public('发布资质公示1', '赵宗召', '资质公示', '自动创建的内容', coverpicture, contentpicture)
        assert '发布资质公示1' in Ba.select_table_publicelement(1, 1, 1).text

        # 发布服务公示

    def test_release_public3(self):
        '''
        发布服务公示
        '''
        Ba = self.successful()
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.release_public('发布物业服务1', '赵宗召', '物业服务', '自动创建的内容', coverpicture, contentpicture)
        assert '发布物业服务1' in Ba.select_table_publicelement(1, 1, 1).text

        # 发布服务公示

    def test_release_public4(self):
        '''
        发布服务公示
        '''
        Ba = self.successful()
        coverpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/1.png'
        contentpicture = '/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png'
        Ba.release_public('发布收费标准1', '赵宗召', '收费标准', '自动创建的内容', coverpicture, contentpicture)
        assert '发布收费标准1' in Ba.select_table_publicelement(1, 1, 1).text

    # 删除服务公示
    def test_delete_public1(self):
        '''
        删除服务公示 取消
        '''

        Ba = self.successful()
        Ba.Enter_the_public()
        time.sleep(5)
        element = Ba.select_table_publicelement(1, 1, 1).text
        Ba.click_delete_button(1, 6, '取消')
        assert element in Ba.select_table_publicelement(1, 1, 1).text

        # 删除服务公示

    def test_delete_public2(self):
        """
         删除服务公示 确定
        """
        Ba = self.successful()
        Ba.Enter_the_public()
        element = Ba.select_table_publicelement(1, 1, 1).text
        Ba.click_delete_button(1, 6, '确定')
        assert element not in Ba.select_table_publicelement(1, 1, 1).text

        # 服务公示标签筛选

    def test_choose_public(self):
        '''
        服务公示标签筛选
        '''
        Ba = self.successful()
        Ba.Enter_the_public()
        Ba.choose_lable_screening('物业服务')
        time.sleep(1)
        Ba.choose_lable_release('未发布')
        time.sleep(5)
        print(Ba.getRownumberCount())
        for i in range(Ba.getRownumberCount()):
            assert '物业服务' == Ba.select_table_publicelement(i, 2, 1).text

    def tearDown(self):
        info('##############################服务公示测试结束#######################################')
        self.driver.close()
        self.driver.quit()
if __name__ == '__main__':
    test_basic1()