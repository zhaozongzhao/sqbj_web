from configparser import ConfigParser
from Util.var import PaserPageObject_path
import re
from Util.var import logobject_path

print(PaserPageObject_path)
class ParsePageObjectRepository(object):

    def __init__(self,pathfile):
        '''

        :param pathfile:  传入配置文件名称
        :type  str
        '''
        self.cf = ConfigParser() #生成解析器
        self.path = PaserPageObject_path.replace('PageObjectRepository',pathfile)
        self.cf.read(self.path,encoding='UTF8') #直接用变量代替


    def getItemSection(self,sectionName):
        '''

        :param sectionName: 传入section
        :return: 返回s该section的所有键值对
        '''
        return  dict(self.cf.items(sectionName))

    def getOptionValue(self,sectionName,optionName):
        '''

        :param sectionName:
        :param optionName:
        :return:  得到section中option的值
        '''
        return self.cf.get(sectionName,optionName)

    def setsectionOptionValue(self,setionName,optionName,value):
        '''

        :param setionName:
        :param optionName:
        :param value:
        :return:  修改配置文件中的信息
        '''
        self.cf.set(setionName, optionName, value)
        self.cf.write(open(logobject_path, "w"))

if __name__ == '__main__':
    pp = ParsePageObjectRepository('logger1.conf')
    # print(pp.getItemSection('Basic_Of_the_public'))
    # print(pp.getOptionValue('Basic_Of_the_public','add_public_button'))
    basic_announcement = pp.getItemSection('handler_hand04')
    print(basic_announcement)
    s= basic_announcement['args']
    # l,h = s.split('>')
    # s = re.sub('log_path','hahahah',s)
    # print(s)
    s = s.replace('log_path','hahahah')
    print(s)
    # print(h)
# # 'LoginPageRepository1.ini'  basic_announcement['lableprompt1']
# /Users/hnbl009/gitfile/webtest/pyhon_zh_web/Action




