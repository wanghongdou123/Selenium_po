from time import sleep
from selenium import webdriver
from  selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self,driver: WebDriver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.get(self.base_url)
        else:
            self.driver = driver

    def close(self):
        sleep(20)
        self.driver.quit()