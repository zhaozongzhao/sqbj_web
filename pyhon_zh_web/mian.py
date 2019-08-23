import unittest
import time
from Util.var import report_path, Testcase_path
from HTMLTestRunner import HTMLTestRunner
import unittest, time
import pytest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%m-%M')
    discover = unittest.defaultTestLoader.discover(Testcase_path, pattern='test_basic_public.py')
    # 新的测试报告
    BeautifulReport(discover).report(filename='智社区测试报告' + now, description='自动换测试', log_path=report_path)

# if __name__ == '__main__':
#     now = time.strftime('%Y-%m-%d %H-%m-%M')
#     filename = report_path + now + 'resul.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(
#         stream=fp,
#         title='自动化测试报告',
#         description='环境: mac 浏览器 ：chome '
#     )
#
#     discover = unittest.defaultTestLoader.discover(Testcase_path,
#                                                    pattern='test*.py')
#     runner.run(discover)
#     fp.close()
