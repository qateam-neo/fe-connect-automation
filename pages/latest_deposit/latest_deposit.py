import time

from pages.base_page import BasePage
from pages.latest_deposit.latest_deposit_locators import LatestDepositLocators


class LatestDepositPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def submit_latest_deposit(self):
        time.sleep(10)
        self.click_success_pop_up_button()
        self.submit_success_case()
        self.click_success_pop_up_button()
        self.click_close_button()

    def click_success_pop_up_button(self):
        success_pop_up_button_locator = LatestDepositLocators.SUCCESS_POP_UP_BUTTON
        self.wait_and_click_element_by_xpath(success_pop_up_button_locator)

    def submit_success_case(self):
        submit_success_case_button_locator = LatestDepositLocators.SUBMIT_SUCCESS_CASE_BUTTON
        self.wait_and_click_element_by_xpath(submit_success_case_button_locator)

    def click_close_button(self):
        close_button_locator = LatestDepositLocators.CLOSE_BUTTON
        self.wait_and_click_element_by_xpath(close_button_locator)