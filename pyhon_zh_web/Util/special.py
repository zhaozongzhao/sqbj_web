
class special:

   def __init__(self,driver):
     self.driver = driver

   def get_alert_name(self):
        '''接收alert'''
        h=self.driver.switch_to_alert().text
        return  h

   def set_alert(self):
       self.driver.switch_to_alert().dismiss()