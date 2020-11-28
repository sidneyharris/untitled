from selenium.webdriver.common.by import By

from test_wechartwork.page.main_page import MainPage


class TestDelMember:
    def setup_class(self):
        self.main = MainPage()

    def test_del_member(self):
        '''
        1.点击通讯录
        2.勾选成员
        3.点击删除
        4.断言已删除成员不在通讯录
        '''
        assert self.main.goto_contact().get_member_id()
