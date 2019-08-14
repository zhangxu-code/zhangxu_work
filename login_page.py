from selenium import webdriver

class TestLogin:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookies = {
            "wwrtx.ltype": "1",
            "wwrtx.d2st": "a8146663",
            "wwrtx.sid": "6TLkIrwNlTt9wxyVdq9wuEbCY5HfNEZ9sUmkffrrEbLrwL-rm7OZMH95zzBO4moC",
            "wxpay.vid": "1688852481994299",
            "wxpay.corpid": "1970325011079243"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()