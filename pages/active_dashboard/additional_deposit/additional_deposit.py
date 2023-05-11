import time

from pages.active_dashboard.additional_deposit.additional_deposit_config import \
    ADDITIONAL_DEPOSIT
from pages.active_dashboard.additional_deposit.additional_deposit_locators import \
    AdditionalDepositPageLocators
from pages.base_page import BasePage


class AdditionalDepositPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def make_additional_deposit(self):
        self.click_blue_button()
        self.click_additional_deposit_button()
        self.fill_additional_deposit()
        self.submit_additional_deposit()


    def click_blue_button(self):
        time.sleep(10)
        blue_button_locator = AdditionalDepositPageLocators.BLUE_BUTTON
        self.wait_and_click_element_by_xpath(blue_button_locator)


    def click_additional_deposit_button(self):
        additional_deposit_button_locator = AdditionalDepositPageLocators.ADDITIONAL_DEPOSIT_BUTTON
        self.wait_and_click_element_by_xpath(additional_deposit_button_locator)

    def fill_additional_deposit(self):
        time.sleep(5)
        additinal_deposit_text_locator = AdditionalDepositPageLocators.ADDITIONAL_DEPOSIT_TEXT
        print(ADDITIONAL_DEPOSIT)
        self.wait_and_click_element_by_xpath(additinal_deposit_text_locator)
        time.sleep(5)
        self.wait_and_fill_element_using_digits(additinal_deposit_text_locator, ADDITIONAL_DEPOSIT)


    def submit_additional_deposit(self):
        additional_deposit_button_locator = AdditionalDepositPageLocators.SUBMIT_BUTTON
        self.wait_and_click_element_by_xpath(additional_deposit_button_locator)
        