import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.MyaccountPage import MyaccountPage
from utility.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestLogIn(BaseClass):

    def test_login(self):
        # print(self.driver.title)
        loginpage = LoginPage(self.driver)
        loginpage.loginlink().click()
        # self.driver.find_element_by_css_selector(".login").click()
        # print(self.driver.title)

        loginpage.email().send_keys("admin@gmail.com")
        # self.driver.find_element_by_css_selector("#email").send_keys("admin@gmail.com")

        loginpage.password().send_keys("admin")
        # self.driver.find_element_by_css_selector("#passwd").send_keys("admin")

        loginpage.signin().click()
        # self.driver.find_element_by_css_selector("#SubmitLogin").click()
        print(self.driver.title)  # My account - My Store

        myaccountPage = MyaccountPage(self.driver)
        myaccountPage.searchbox().send_keys("shirt")
        # self.driver.find_element_by_css_selector("#search_query_top").send_keys("shirt")
        # //li[@class='ac_even ac_over']

        myaccountPage.searchresult().click()
        # shirt = self.driver.find_element_by_xpath("//div[@class='ac_results']//li")
        # driver.find_element_by_xpath("//li[@class='ac_even ac_over']")
        # WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.XPATH(shirt)))
        # driver.find_element_by_xpath("//div[@class='ac_results']//li").click()
        # shirt.click()
        # for menu in menus:
        #     #if "shirt" in menu.text:
        #         #menu.click()
        #     print(menu.text)
        #
        print(self.driver.title)
        itemName = self.driver.find_element_by_xpath("//div//h1").text
        dollarprice = self.driver.find_element_by_css_selector("#our_price_display").text
        # remove $ sign from price
        p = str(dollarprice)
        itemPrice = p.replace("$", "")
        print(itemPrice)

        self.driver.find_element_by_css_selector("button[class = 'exclusive']").click()
        self.driver.find_element_by_link_text("Proceed to checkout").click()
        print(self.driver.title)
        itemNameOrderPage = str(self.driver.find_element_by_xpath("//td/p/a").text)

        assert itemNameOrderPage == itemName, "item name did not match"

        tp = str(self.driver.find_element_by_xpath("//*[contains(@class,'cart_item')]//td[6]/span").text)
        totalPrice = tp.replace("$", "")

        assert totalPrice == itemPrice
        self.driver.find_element_by_css_selector(".standard-checkout").click()
        self.driver.find_element_by_name("processAddress").click()
        self.driver.find_element_by_name("cgv").click()
        self.driver.find_element_by_css_selector(".standard-checkout").click()

        # self.driver.close()
