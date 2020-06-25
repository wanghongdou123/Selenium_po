from selenium.webdriver.common.by import By
from test_selenium.page.base_page import BasePage

class Register(BasePage):
    def register(self,corpname):
        # 企业名称
        self.driver.find_element(By.ID,"corp_name").send_keys(corpname)
        # 行业类型
        self.driver.find_element(By.XPATH,"//*[@id='corp_industry']").click()
        # IT服务
        self.driver.find_element(By.LINK_TEXT,"IT服务").click()
        self.driver.find_element(By.XPATH,'//*[@id="corp_industry"]/div/table/tbody/tr/td[2]/div[1]/div[1]/a').click()
        # 人员规模
        self.driver.find_element(By.XPATH,"//*[@id='corp_scale_btn']").click()
        self.driver.find_element(By.XPATH,"//*[@id='corp_scale_btn']/div/ul/li[1]/a/span[2]")
        # 管理员姓名
        self.driver.find_element(By.ID,'manager_name').send_keys("测试")
        # 手机号
        self.driver.find_element(By.ID,'register_tel').send_keys('13511111111')
        self.driver.find_element(By.ID,'submit_btn').click()
        return self

    def get_error_message(self):
        result = []
        for element in self.driver.find_elements(By.CSS_SELECTOR,'js_error_msg'):
            result.append(element.text)


        return result