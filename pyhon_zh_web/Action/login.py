from pageobject.login_page import *
from selenium import webdriver




def login(driver,userename,passord):

    lp = LoginPage(driver)
    lp.getUserName().send_keys(userename)
    lp.getPassword().send_keys(passord)
    try:
        lp.getProjectinput().click()
        #当账户属于多个租户
        if len(lp.gettenant())>1:
                lp.getProjectvalue().click()
        time.sleep(3)
    except Exception as e:
       lp.getLoginButton().click()
    lp.getLoginButton().click()

#获取登陆失败提示
def geterror(driver):
    lp = LoginPage(driver)
    try:
        error = lp.getuserorpassworderror()
    except Exception as E:
        print(E)
    else:
         return error.text


if __name__ == '__main__':
    #测试代码
    driver =  webdriver.Chrome()
    driver.get('http://smart.sit2.sqbj.com/portal/login')
    login(driver,'18301565568','111111')
    print(geterror(driver))
    driver.quit()