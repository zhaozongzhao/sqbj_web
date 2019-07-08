from configparser import ConfigParser
from Util.var import PaserPageObject_path

print(PaserPageObject_path)
class ParsePageObjectRepository(object):

    def __init__(self,pathfile):
        self.cf = ConfigParser() #生成解析器
        self.path = PaserPageObject_path.replace('PageObjectRepository',pathfile)
        self.cf.read(self.path,encoding='UTF8') #直接用变量代替


    def getItemSection(self,sectionName):
        return  dict(self.cf.items(sectionName))

    def getOptionValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)

if __name__ == '__main__':
    pp = ParsePageObjectRepository('BasicserverRepository.ini')
    print(pp.getItemSection('Basic_announcement_home'))
    print(pp.getOptionValue('Basic_announcement_home','lableprompt1'))
    basic_announcement = pp.getItemSection('Basic_announcement_home')

    l,h = basic_announcement['lableprompt1'].split('>')
    print(l)
    print(h)
# # 'LoginPageRepository1.ini'  basic_announcement['lableprompt1']
# /Users/hnbl009/gitfile/webtest/pyhon_zh_web/Action




