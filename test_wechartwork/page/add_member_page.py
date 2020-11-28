from time import sleep

from selenium.webdriver.common.by import By
from test_wechartwork.page.base_page import BasePage
from test_wechartwork.page.contact_page import ContactPage

class AddMemberPage(BasePage):
    _username = "username"  # 用户名
    _phonemember = "memberAdd_phone"  # 手机号
    _id = "memberAdd_acctid"  # id
    _save = ".js_btn_save"  # 下方保存按钮
    _cancle = '.js_btn_cancel'  # 取消按钮

    def add_member(self):
        '''
        添加成员,返回到Contact页面
        :return:
        '''
        self.find(By.ID, self._username).send_keys("维恩1")
        self.find(By.ID, self._id).send_keys("111223")
        self.find(By.ID, self._phonemember).send_keys("13811112226")
        self.find(By.CSS_SELECTOR, self._save).click()
        sleep(3)
        return ContactPage(self.driver)

    def add_member_fail(self):
        ''''''
        self.find(By.ID, self._username).send_keys("维恩2")
        self.find(By.ID, self._id).send_keys("111224")
        self.find(By.ID, self._phonemember).send_keys("13811112227")
        self.find(By.CSS_SELECTOR, self._save).click()
        self.find(By.CSS_SELECTOR, self._cancle).click()
        return ContactPage(self.driver)


