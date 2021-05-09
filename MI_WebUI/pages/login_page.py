from pages.base_page import  BasePage


class LoginPage(BasePage):

    username_ipt = ('name','account')
    password_ipt = ('name','password')
    login_btn = ('class name','mi-button')

    def input_username(self,username):
        print(f'输入用户名{username}')
        self.input_to(*self.username_ipt,username)

    def input_password(self,password):
        self.input_to(*self.password_ipt,password)

    def click_login_btn(self):
        self.click(*self.login_btn)

    def login(self,username,password):
        """组合操作-登录"""
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()