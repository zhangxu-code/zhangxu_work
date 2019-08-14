from time import sleep

from selenium.webdriver.common.by import By

from test_wework.base_page import BasePage
from test_wework.login_page import TestLogin


class TestAddImage(BasePage):
    def __init__(self, wework: TestLogin):
        self._driver = wework.driver

    def add_image(self):
        self._driver.find_element(By.XPATH, '//*[text()="管理工具"]').click()
        self.click_by_js(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/ul/li[5]/a/span")
        sleep(3)
        self.click_by_js(By.PARTIAL_LINK_TEXT, "图片")
        sleep(2)
        self.click_by_js(By.XPATH, '/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div/div/div[1]/div[1]/a')
        self.find(By.XPATH, '//*[@id="js_upload_input"]').send_keys('C:\\Windows\\a.png')
        self._driver.implicitly_wait(10)

        self.click_by_js(By.XPATH, '//*[text()="完成"]')
        