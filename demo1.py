# 实战：
# 1、百度搜索"霍格沃兹测试学院"
# 2、点击搜索
# 3、点击"霍格沃兹测试学院_腾讯课堂"
# 4、点击"名企定向培养"

from selenium import webdriver

class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get('https://www.baidu.com')
        # 在输入框中输入霍格沃兹测试学院
        self.driver.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
        # 点击百度一下
        self.driver.find_element_by_id('su').click()
        # 使用link_text点击
        self.driver.find_element_by_link_text('霍格沃兹测试学院_腾讯课堂').click()
        # 将获取到的window_handles赋值给一个变量handles
        handles = self.driver.window_handles
        # 打印handles，查看当前有几个窗口
        print(handles)
        # 切换句柄
        self.driver.switch_to.window(handles[-1])
        # 点击
        self.driver.find_element_by_partial_link_text('名企定向培养').click()



