# a = int(input())
# e = a//2
# for i in range(e,-1,-1):
#     print(' '*i,'*'*(a-2*i), ' '*i)

#
# 'jsx-3914091371 block display'
# 'jsx-3914091371 block display'
# h = "/Users/hnbl009/gitfile/webtest/pyhon_zh_web/Conf/PageobjectRepository"
# list = h.replace('PageobjectRepository','LoginPageRepository.ini')
# print(list)
# import unittest
#
# class Test_login(unittest.TestCase):
#
#     def test_1ss1(self):
#         print(1)
#
# #     def test_2as2(self):
# #         print(2)
#
#
# aim_list= [1,2,2,20,5.6,8.9,["a","b","c"],"xyz"]
#
#
# import random
# passwd = random.sample("0123456789",6)
#
# result = "".join(passwd)  #join 用指定方法生成字符串
# print(result)
# # print(
# #     set(
# #         list
# #         (zip
# #          (list
# #           (map
# #            (lambda x:type(x),aim_list)),
# #           [list
# #            (map
# #             (lambda x: type(x), aim_list)).count(i)
# #            for i in list(
# #               map(lambda x: type(x), aim_list)
# #           )]))))
#
# #
# # 01 文件名去重复
# #
# # 02 选出文件大于10m的
# #
# # 03 获取到文件的md5值，然后利用这个md5值对文件名进行重命名（其中md5代表一个文件属性）
# #
# # 04 打印出最后的符合条件的所有文件名
# import os
# pathfile =  '/Users/hnbl009/gitfile/webtest/pyhon_zh_web'
# for i,a,b in os.walk(pathfile):
#     print(i)  #当前目录路径
#     print(a)  #当前路径下所有子目录
#     print(b)  #当前路径下所有非目录子文件
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.baidu.com')
driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi.png')