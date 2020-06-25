from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.login import Login
from test_selenium.page.register import Register


class Index(BasePage):
    base_url = 'https://work.weixin.qq.com/'

    # 进入注册页
    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT,"立即注册").click()
        return Register(self.driver)

    # 进入登录页
    def goto_login(self):
        self.driver.find_element(By.LINK_TEXT,"企业登录").click()
        return Login(self.driver)