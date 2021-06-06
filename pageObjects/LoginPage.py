from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        print("LoginPage Constructor is executed")
        self.driver = driver

    loginlocator = (By.CSS_SELECTOR, ".login")
    # self.driver.find_element_by_css_selector(".login").click()

    def loginlink(self):
        print(" **** loginlink method is executed")
        return self.driver.find_element(*LoginPage.loginlocator)
