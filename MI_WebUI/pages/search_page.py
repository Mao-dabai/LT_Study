from pages.base_page import BasePage


class SearchPage(BasePage):
    search_ipt = ('id', 'search')
    search_btn = ('class name', 'search-btn')

    def input_search(self,search_key):
        print(f'输入搜索内容{search_key}')
        self.input_to(*self.search_ipt, search_key)

    def click_search_btn(self):
        self.click(*self.search_btn)

    def search(self,search_key):
        self.input_search(search_key)
        self.click_search_btn()
