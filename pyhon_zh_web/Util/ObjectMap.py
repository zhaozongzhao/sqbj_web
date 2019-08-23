from selenium.webdriver.support.ui import WebDriverWait

from Util.log import *


#获取单个元素对象
def getElement(driver,locatetype,locatorExpression):
    info('定位类型{},定位地址{}'.format(locatetype,locatorExpression))
    try:
        element = WebDriverWait(driver,10,0.5).until(lambda x:x.find_element(by=locatetype,value= locatorExpression))
        return element
    except Exception as e:
        raise e


#获取多个相同页面元素对象,用list返回
def getElements(driver,locatetype,locatorExpression):
    info('定位类型{},定位地址{}'.format(locatetype,locatorExpression))
    try:

        elements = WebDriverWait(driver,5,0.5).until(lambda x:x.find_elements(by=locatetype,value=locatorExpression))
        return elements
    except  Exception as e:
        raise e

    driver.find_elements


