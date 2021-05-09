from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class BasePage:
    def __init__(self, driver: webdriver.Chrome, url=None, frame=None):
        self.driver = driver
        self.url = url
        self.frame = frame
        self.open()  # 如果配置了url, 则自动打开，如果有frame则自动切换进入

    def wait(self, sec=1):
        sleep(sec)

    def open(self):
        """打开页面"""
        if self.url:
            self.driver.get(self.url)
        # if self.frame:
        #     self.driver.switch_to.default_content()
        #     self.driver.switch_to.frame(self.frame)

    def find(self, by, value):
        if by == 'text':
            by = 'xpath'
            value = f'//*[text()="{value}"]'
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            print(f'定位不到元素 {by}={value}')
            self.driver.save_screenshot('reports/{by}_{value}.png')
            raise

    def click(self, by, value):
        print(f'点击 {by}={value}')
        self.find(by, value).click()

    def input_to(self, by, value, text):
        print(f'在 {by}={value} 中输入 {text}')
        self.find(by, value).send_keys(text)