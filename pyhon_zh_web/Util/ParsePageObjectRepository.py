from configparser import ConfigParser
from Util.var import PaserPageObject_path

print(PaserPageObject_path)
class ParsePageObjectRepository(object):

    def __init__(self):
        self.cf = ConfigParser() #生成解析器
        self.cf.read(PaserPageObject_path,encoding='UTF8') #直接用变量代替

    def getItemSection(self,sectionName):
        return  dict(self.cf.items(sectionName))

    def getOptionValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)

if __name__ == '__main__':
    pp = ParsePageObjectRepository()
    print(pp.getItemSection('zh_login_page'))
    print(pp.getOptionValue('zh_login_page','login_page.username'))






