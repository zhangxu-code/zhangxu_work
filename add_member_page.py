from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_wework.base_page import BasePage
from test_wework.login_page import TestLogin


class AddMember(BasePage):
    def __init__(self, wework: TestLogin):
        self._driver = wework.driver
    def add_member(self, name, alias, phone):
        self._driver.find_element(By.XPATH, '//*[text()="通讯录"]').click()
        self._driver.implicitly_wait(10)

        self.click_by_js(By.XPATH, '//*[text()="添加成员"]')
        # self.click_by_js(By.CSS_SELECTOR, '.ww_icon.ww_icon_CameraWhiteSmall')
        # self.find(By.XPATH, '/html/body/form/div/div[2]/div/div[1]/div[2]/a/input').send_keys('C:\\Windows\\a.png')
        # self.click_by_js(By.XPATH, "/html/body/form/div/div[3]/a[1]")
        # self._driver.implicitly_wait(10)

        self.find(By.ID, 'username').send_keys(name)
        self.find(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(alias)
        self.find(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phone)
        self._driver.implicitly_wait(10)
        self.click_by_js(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[1]/a[2]")
        assert self.find(By.ID,"js_tips").text == '保存成功'