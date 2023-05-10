import time

from pages.active_dashboard.withdrawal.withdrawal_config import \
    WithdrawalConfig
from pages.active_dashboard.withdrawal.withdrawal_locators import \
    WithdrawalPageLocators
from pages.base_page import BasePage


class WithdrawalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.is_full_withdrawal = WithdrawalConfig.IS_FULL_WITHDRAWAL

    def make_withdrawal(self):
        self.click_blue_button()
        self.click_withdrawal_button()
        if self.is_full_withdrawal:
            self.choose_full_withdrawal()
        else:
            self.choose_partial_withdrawal()
            
        self.click_withdrawal_purpose()
        self.submit_withdrawal()
        self.click_done_button()


    def click_blue_button(self):
        time.sleep(10)
        blue_button_locator = WithdrawalPageLocators.BLUE_BUTTON
        self.wait_and_click_element_by_xpath(blue_button_locator)

    def click_withdrawal_button(self):
        withdrawal_option_button_locator = WithdrawalPageLocators.WITHDRAWAL_OPTION_BUTTON
        self.wait_and_click_element_by_xpath(withdrawal_option_button_locator)

    def choose_full_withdrawal(self):
        full_withdrawal_button_locator = WithdrawalPageLocators.FULL_WITHDRAWAL_OPTION
        self.wait_and_click_element_by_xpath(full_withdrawal_button_locator)
        self.click_continue_button()

    def choose_partial_withdrawal(self):
        time.sleep(5)
        partial_withdrawal_button = WithdrawalPageLocators.PARTIAL_WITHDRAWAL_OPTION
        self.wait_and_click_element_by_xpath(partial_withdrawal_button)
        self.click_continue_button()
        self.fill_partial_withdrawal()

    def fill_partial_withdrawal(self):
        time.sleep(5)
        partial_withdrawal_text = WithdrawalPageLocators.PARTIAL_WITHDRAWAL_TEXT
        partial_withdrawal_amount = WithdrawalConfig.PARTIAL_WITHDRAWAL_AMOUNT
        self.wait_and_fill_element_using_digits(partial_withdrawal_text, partial_withdrawal_amount)

    def click_continue_button(self):
        continue_button_locator = WithdrawalPageLocators.CONTINUE_BUTTON
        self.wait_and_click_element_by_xpath(continue_button_locator)
        
    def click_withdrawal_purpose(self):
        withdrawal_purpose_combo_locator = WithdrawalPageLocators.WITHDRAWAL_PURPOSE_COMBO
        self.wait_and_click_element_by_xpath(withdrawal_purpose_combo_locator)

        withdrawal_purpose_item_locator = WithdrawalPageLocators.WITHDRAWAL_PURPOSE_ITEM
        self.wait_and_click_element_by_xpath(withdrawal_purpose_item_locator)

    def submit_withdrawal(self):
        submit_withdrawal_button_locator = WithdrawalPageLocators.SUBMIT_WITHDRAWAL_BUTTON
        self.wait_and_click_element_by_xpath(submit_withdrawal_button_locator)
        
    def click_done_button(self):
        done_button_locator = WithdrawalPageLocators.DONE_BUTTON
        self.wait_and_click_element_by_xpath(done_button_locator)
        