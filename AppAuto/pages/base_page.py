from appium import  webdriver

class BasePage:
    def __init__(self,driver:webdriver.Remote):
        self.driver = driver

    def click_element(self,by,value):
        print(f"点击元素:{by}={value}")

        self.driver.find_element(by,value).click()

    def input_text(self,by,value,text):
        print(f"在元素{by}={value}中输入{text}")
        self.driver.find_element(by,value).send_keys(text)


