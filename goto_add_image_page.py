from time import sleep

from selenium.webdriver.common.by import By
from test_wework.base_page import BasePage
from test_wework.login_page import TestLogin


class GoTestAddImage(BasePage):
    def __init__(self, wework: TestLogin):
        self._driver = wework.driver

    def goto_add_image(self):
        self._driver.find_element(By.XPATH, '//*[text()="管理工具"]').click()
        self.click_by_js(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/ul/li[5]/a/span")
        sleep(3)
        self.click_by_js(By.PARTIAL_LINK_TEXT, "图片")
