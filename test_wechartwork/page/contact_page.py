from time import sleep

from selenium.webdriver.common.by import By

from test_wechartwork.page.base_page import BasePage


class ContactPage(BasePage):
    _member_name = '.member_colRight_memberTable_td:nth-child(2)'  # 成员姓名信息
    _del = '.js_delete'  # 删除按钮
    _id_elements = '.ww_checkbox'  # 成员列表
    _del_confirm = '.ww_btn_Blue'  # 确认按钮
    _import_but = '//div[@class="ww_operationBar"]/div[2]'  # 批量导入
    _js_import = '文件导入'  # 文件导入
    _file_import = '.ww_fileImporter_fileContainer_uploadInputMask'  # 文件上传
    _file_link = r"E:\Wechat\test_selenium\contact.xlsx"
    _import = '.ww_fileImporter_submit'  # 导入
    _done = '//div[@class="ww_fileImporter_successBtnWrap"]/a[1]'  # 完成
    # 获取成员列表
    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR, self._member_name)
        # 通过for循环拿到title,append--列表推导式
        name_list = [element.get_attribute("title") for element in elements]
        return [name_list]

    # 获取成员id列表
    def get_member_id(self):
        elements = self.finds(By.CSS_SELECTOR,
                              ".member_colRight_memberTable_td:nth-child(1)")
        id_list = [element.get_attribute("title") for element in elements]
        self.find(By.CSS_SELECTOR, self._id_elements).click()  # 点击成员列表
        self.find(By.CSS_SELECTOR, self._del).click()  # 点击删除
        # 点击确认按钮
        return [id_list]
    # 导入文件
    def import_member_file(self):
        self.find(By.XPATH, self._import_but).click()  # 批量导入
        self.driver.implicitly_wait(3)
        self.find(By.LINK_TEXT, self._js_import).click()  # 文件导入
        self.driver.implicitly_wait(3)
        self.find(By.CSS_SELECTOR, self._file_import).send_keys(self._file_link)  # 上传文件
        self.driver.implicitly_wait(3)
        self.find(By.CSS_SELECTOR, self._import).click()  # 点击导入
        self.driver.implicitly_wait(5)
        self.find(By.XPATH, self._done).click()  # 点击完成

