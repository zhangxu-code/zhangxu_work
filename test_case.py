from time import sleep

import allure

from test_wework.add_image_page import TestAddImage
from test_wework.add_member_page import AddMember
from test_wework.goto_add_image_page import GoTestAddImage
from test_wework.login_page import TestLogin
from test_wework.base_page import BasePage
from test_wework.profile_page import TestProfile

class TestHome():
    def setup(self):
        self.login = TestLogin()
        self.addmem = AddMember(self.login)
        self.profile = TestProfile(self.login)
        self.go_image = GoTestAddImage(self.login)
        self.add_image = TestAddImage(self.login)

    def teardown(self):
        sleep(3)
        self.login.quit()

    @allure.feature('添加人员')
    @allure.title("添加人员")
    def test_add_member(self, addmem=None):
        self.addmem.add_member( "tester02", "tester02", "13711112222")
        self.addmem.get_tips("保存成功")

    @allure.feature('搜索页')
    @allure.title("搜索人员")
    def test_search(self):
        self.profile.search('tester02')
        self.profile.get_result("编辑")

    @allure.feature('搜索页')
    @allure.title("编辑人员")
    def test_edit(self):
        self.profile.edit("tester")
        self.addmem.get_tips("保存成功")

    @allure.feature('搜索页')
    @allure.title("禁用人员")
    def test_unable(self):
        self.profile.unable("tester")
        self.addmem.get_tips("禁用成功")

    @allure.feature('搜索页')
    @allure.title("删除人员")
    def test_delete(self):
        self.profile.delete("tester")
        self.addmem.get_tips("删除成功")

    @allure.feature('goto添加图片')
    @allure.title("goto添加图片")
    def test_goto_add_image(self):
        self.go_image.goto_add_image()
        self.profile.get_result("添加图片")

    @allure.feature('添加图片')
    @allure.title("添加图片")
    def test_add_image(self):
        self.add_image.add_image()
        self.profile.get_result("a.png")