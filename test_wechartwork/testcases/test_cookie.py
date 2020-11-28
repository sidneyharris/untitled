import json
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_wechartwork.page.main_page import MainPage


class TestCookie:

    def setup(self):
        self.main = MainPage()

    def test_get_cookie(self):#获取cookies保存到cookie.json里
        sleep(10)
        cookies = self.main.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

    def test_cookie_login(self):#打开cookie
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:

            self.main.driver.add_cookie(cookie)

        while True:
            self.main.driver.refresh()
            #显示等待
            res = WebDriverWait(self.main.driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if res is not None:
                break