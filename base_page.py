from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver: WebDriver):
        self._driver=driver

    def find(self,*locator):
        return self._driver.find_element(*locator)

    def click_by_js(self, by, locator):
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable((by, locator)))
        self._driver.execute_script("arguments[0].click();",self._driver.find_element(by, locator))

    def get_tips(self, remainder):
        self._driver.implicitly_wait(5)
        assert  remainder in self._driver.find_element(By.ID, "js_tips").text,"执行失败"
        print("执行成功")

    def get_result(self,result):
        sleep(2)
        assert result in self._driver.page_source
        print("执行成功")
