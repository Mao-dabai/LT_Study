from pages.base_page import BasePage


class CategoryPage(BasePage):
    xiaomi_mobile_loc = ("xpath","//*[@text='小米手机']")

    def click_xiaomi_mobile(self):
        """点击小米手机"""
        self.click_element(*self.xiaomi_mobile_loc)
