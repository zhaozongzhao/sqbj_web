import unittest,time
from Action.basic_announcementlist import *
from Action.page_home import *
from Action.login import *
from Util.Excel import *
from Util.var import *
from Util.special import *

class test_basic(unittest.TestCase):
    def setUp(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # self.driver = webdriver.Chrome(driver_path= '' ,chrome_options=chrome_options,
        #         service_args=['--verbose', '--log-path=<path-to-log>/chromedriver.log'])
        self.driver = webdriver.Chrome()
        self.driver.get('http://smart.sit2.sqbj.com/portal/login')
        self.pe = parseExcel(Excelobject_path)
        # self.alert = special(self.driver)
        login(self.driver,'18301565568','111111')

    def test_1(self):
        self.driver.save_screenshot('1.png')


    def tearDown(self):
        self.driver.close()

