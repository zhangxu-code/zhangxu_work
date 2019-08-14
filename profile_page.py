from time import time, sleep

from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_wework.login_page import TestLogin
from test_wework.base_page import BasePage


class TestProfile(BasePage):
    def __init__(self, wework: TestLogin):
        self._driver = wework.driver

    def search(self,key):
        self.find(By.XPATH, '//*[text()="通讯录"]').click()
        sleep(2)
        self.find(By.ID, 'memberSearchInput').clear()
        self.find(By.ID, 'memberSearchInput').send_keys(key)

    def edit(self,name):
        self.search(name)
        #WebDriverWait(self, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[text()="编辑"]')))
        self.click_by_js(By.XPATH, '//*[text()="编辑"]')
        self.find(By.ID,'username').clear()
        udid=str(time())
        self.find(By.ID, 'username').send_keys("tester"+udid)
        self.click_by_js(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[1]/a[1]")

    def unable(self,name):
        self.search(name)
        #WebDriverWait(self, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[text()="编辑"]')))
        self.click_by_js(By.CSS_SELECTOR,'.qui_btn.ww_btn.js_disable')
        self.click_by_js(By.XPATH, '//*[text()="确认"]')

    def delete(self,name):
        self.search(name)
        #WebDriverWait(self, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[text()="编辑"]')))
        self._driver.implicitly_wait(5)
        self.click_by_js(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_del_member')
        self.click_by_js(By.XPATH, '//*[text()="确认"]')
