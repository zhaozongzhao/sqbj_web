# encoding = utf-8
import logging
import logging.config
import re
from Util import var
from Util.ParsePageObjectRepository import ParsePageObjectRepository

#修改日志配置文件中的存放地址
pp = ParsePageObjectRepository('logger1.conf')
handlist = []
handlist.append(pp.getItemSection('handler_hand04'))
handlist.append(pp.getItemSection('handler_hand03'))
log_path = var.logfile_path
hand04 = handlist[0]['args'].replace('log_path',log_path + 'info.log')
hand03 = handlist[1]['args'].replace('log_path',log_path + 'error.log')
print(hand04)
pp.setsectionOptionValue('handler_hand04' ,'args',hand04)
pp.setsectionOptionValue('handler_hand03','args',hand03)

# # log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logger1.conf')
#从指定的fname的配置文件中读取logging配置文件，文件格式参见
logging.config.fileConfig(var.logobject_path, defaults=None, disable_existing_loggers=True)

def debug(message):
     #打印debug级别的日志
     logging.debug(message)

def warning(message):
     #打印warning级别的日志
     logging.warning(message)

def info(message):
     #打印info级别的日志
     logging.info(message)

info('验证测试数据哈哈哈')


