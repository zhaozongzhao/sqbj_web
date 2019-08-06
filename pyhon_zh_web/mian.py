from HTMLTestRunner import HTMLTestRunner
import unittest,time
import pytest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
     now=time.strftime('%Y-%m-%d %H-%m-%M')
     # filename='/Users/hnbl009/gitfile/webtest/pyhon_zh_web/HtmlRoport/'+now+'resul.html'
     filename='/Users/hnbl009/gitfile/webtest/pyhon_zh_web/HtmlRoport/'
     # fp = open(filename,'wb')
     # runner = HTMLTestRunner(
     #     stream=fp,
     #     title='自动化测试报告',
     #     description='环境: mac 浏览器 ：chome '
     # )

     discover = unittest.defaultTestLoader.discover('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/testcase/',pattern = 'test_basic_public.py')

     # runner.run(discover)
     # fp.close()

     #新的测试报告
     BeautifulReport(discover).report(filename='测试',description='自动换测试',log_path=filename)