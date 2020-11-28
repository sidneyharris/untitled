# 从selenium导入webdriver
from selenium import webdriver
# 导入Options
from selenium.webdriver.chrome.options import Options

#Basepage定义式，它是一个其他page的公共方法的封装，它是一个底层使用的框架
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    '''_base_url放到mainpage避免在BasePage泄露底层代码'''
    _base_url = ""
    def __init__(self, driver_basepage:WebDriver = None):
        # 如果driver_basepage为None
        if driver_basepage == None:
            # 实例化options
            option = Options()
            # option.add_experimental_option('w3c',False)
            # cmd: chrome --remote-debugging-port=9222
            # 需要和启动命令的端口号一致
            # 指定了一个调试地址9222
            option.debugger_address = "localhost:9222"
            # 传递option,调用driver等于webdriver.Chrome
            self.driver = webdriver.Chrome(options=option)
        #不为None，等于传入的driver
        else:
            self.driver = driver_basepage
        # 如果_base_url 不为空，获取_base_url
        if self._base_url != "":

            self.driver.get(self._base_url)
        # 等待3s
        self.driver.implicitly_wait(3)
        # 最大化窗口
        self.driver.maximize_window()
    '''二次封装'''
    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def finds(self, by, value):
        return self.driver.find_elements(by=by, value=value)

    def quit(self):
        # return self.driver.quit()
        pass
