import os

# 获取项目的绝对路径
path = os.path.dirname(os.path.dirname(__file__))

# 配置文件路径（获取对象库文件的绝对路径）
PaserPageObject_path = path + '/Conf/PageObjectRepository'

# 数据表格路径
Excelobject_path = path + '/testdata/工作簿2.xlsx'

# 日志文件
logobject_path = path + '/Conf/logger1.conf'
logfile_path = path + '/logs/logs/'

#报告地址
report_path =  path + '/HtmlRoport/'

#测试用例的地址
Testcase_path =  path + '/testcase/'

