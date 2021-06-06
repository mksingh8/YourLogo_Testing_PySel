from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        print("LoginPage Constructor is executed")
        self.driver = driver

    loginlocator = (By.CSS_SELECTOR, ".login")
    # self.driver.find_element_by_css_selector(".login").click()
    emaillocator = (By.CSS_SELECTOR, "#email")
    passwordlocator = (By.CSS_SELECTOR, "#passwd")
    signinBtnlocator = (By.CSS_SELECTOR, "#SubmitLogin")


    def loginlink(self):
        print(" **** loginlink method is executed")
        return self.driver.find_element(*LoginPage.loginlocator)

    def email(self):
        print(" **** email method is executed")
        return self.driver.find_element(*LoginPage.emaillocator)

    def password(self):
        return self.driver.find_element(*LoginPage.passwordlocator)

    def signin(self):
        return self.driver.find_element(*LoginPage.signinBtnlocator)


