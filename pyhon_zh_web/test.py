# a = int(input())
# e = a//2
# for i in range(e,-1,-1):
#     print(' '*i,'*'*(a-2*i), ' '*i)

#
# 'jsx-3914091371 block display'
# 'jsx-3914091371 block display'
# h = "/Users/hnbl009/gitfile/webtest/pyhon_zh_web/Conf/PageobjectRepository"
# list = h.replace('PageobjectRepository','LoginPageRepository1.ini')
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
# from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.baidu.com')
# driver.save_screenshot('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/logs/ceshi1.png')
# from configparser import ConfigParser
# conf = ConfigParser()
# conf.read('/Users/hnbl009/gitfile/webtest/pyhon_zh_web/Conf/LoginPageRepository1.ini')       # 文件路径
# name = conf.get('zh_login_page','login_page.username')
# dict = {'announcement.page': "xpath>//span[contains(text(),'小区信息管理')]", 'announcement.list': 'xpath>//*[@id="0$Menu"]/li[1]', 'announcement.analysis': "xpath>//span[contains(text(),'公告分析')]", 'public.list': "xpath>//span[contains(text(),'服务公示列表')]", 'announcement.page.communityselect': 'xpath>//li[@role="option"]', 'lableprompt1': "xpath>//li[contains(text(),'温馨提示')]", 'announcement.page.communitynotice': "xpath>//li[contains(text(),'紧急通知')]", 'announcement.page.communitypropaganda': "xpath>//li[contains(text(),'小区宣传')]", 'announcement.page,lableinput': 'xpath>//input[@placeholder="请输入标题内容"]', 'add_announcement_button': "xpath>//span[contains(text(),'新建公告')]/..", 'add_announcement_inputlable': 'xpath>//input[@placeholder="请输入标题"]', 'add_announcement_inputissuer': 'xpath>//input[@placeholder="请输入发布方"]', 'set_lable_announcement': 'xpath>//*[@id="layout"]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div/span/div/div', 'add_announcement_inputcover': 'xpath>//*[@id="layout"]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div/span/div/span/div[2]/span', 'add_announcement_div': 'xpath>//*[@id="layout"]/div/div/div/div[2]/div[1]/form/div[7]/div[2]/div/span/div/div/div[2]/div/div/div', 'save_announcement': "xpath>//span[contains(text(),'保 存')]/..", 'preview_announcement': "xpath>//button/span[contains(text(),'预 览')]", 'release_announcement': "xpath>//button/span[contains(text(),'发 布')]", 'cancel_announcement': "xpath>//button/span[contains(text(),'取 消')]"}
# print(dict['lableprompt1'])
i=0
while False :
           i=i+1
           print(i)