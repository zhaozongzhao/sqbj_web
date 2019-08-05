import unittest
import time
from Util.var import report_path,Testcase_path

# import pytest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%m-%M')
    filename = report_path + now + 'resul.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        description='环境: mac 浏览器 ：chome '
    )

    discover = unittest.defaultTestLoader.discover(Testcase_path,
                                                   pattern='test*.py')
    runner.run(discover)
    fp.close()
