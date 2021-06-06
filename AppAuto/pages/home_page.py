from pages.base_page import BasePage


class HomePage(BasePage):
    # 1.传入driver，绑定对象
    # 2.列出所有元素
    # 3.每个元素操作编写一个方法
    # 4.根据需求封装一些组合操作方法

    category_loc = ("xpath","//*[@text='分类']")

    def click_category(self):
        """点击分类"""
        # self.driver.find_element_by_xpath("//*[@text='分类']").click()
        self.click_element(*self.category_loc)