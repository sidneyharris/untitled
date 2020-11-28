from test_wechartwork.page.add_member_page import AddMemberPage
from test_wechartwork.page.base_page import BasePage
from test_wechartwork.page.contact_page import ContactPage


from selenium.webdriver.common.by import By

# 主页
class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # 添加成员按钮
    _addmember = '.index_service_cnt_itemWrap:nth-child(1)'
    # 通讯录
    _contact = 'menu_contacts'
    # 跳转，函数名可以命名为goto_xxx
    def goto_add_member(self):#点击添加成员,跳转到AddMember页面
        # click
        self.find(By.CSS_SELECTOR, self._addmember).click()
        return AddMemberPage(self.driver)

    def goto_contact(self):
        self.find(By.ID, self._contact).click()
        return ContactPage(self.driver)

    def goto_import_contact(self):
        pass