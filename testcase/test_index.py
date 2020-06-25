from test_selenium.page.index import Index

class TestIndex:
    def setup(self):
        self.index = Index()

    # 对注册功能的测试
    def test_register(self):
        self.index.goto_register().register("测试学院")


    # 对login功能进行测试
    def test_login(self):
        # 从首页进入到注册页
        register_page = self.index.goto_login().goto_registry().register("测试")
        assert "请选择" in "|" .join(register_page.get_error_message())


    # 关闭driver
    def teardown(self):
        self.index.close()
