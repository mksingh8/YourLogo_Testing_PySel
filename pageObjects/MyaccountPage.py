from selenium.webdriver.common.by import By


class MyaccountPage:
    def __init__(self, driver):
        print("MyAccount page Constructor is executed")
        self.driver = driver

    searchboxlocator = (By.CSS_SELECTOR, "#search_query_top")
    searchresultlocator = (By.XPATH, "//div[@class='ac_results']//li")

    def searchbox(self):
        return self.driver.find_element(*MyaccountPage.searchboxlocator)

    def searchresult(self):
        return self.driver.find_element(*MyaccountPage.searchresultlocator)
