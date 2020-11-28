from selenium.webdriver.common.by import By

from test_wechartwork.page.main_page import MainPage


class TestImportFile:
    def setup_class(self):
        self.main = MainPage()

    def test_import_file(self):
        self.main.goto_contact().import_member_file()