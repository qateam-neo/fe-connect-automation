import time

from apis.activation.activation import ClientActivateAPI
from apis.get_client_id.get_client_id import GetClientIdAPI
from pages.base_page import BasePage
from pages.initial_deposit.initial_deposit_config import InitialDepositConfig
from pages.initial_deposit.initial_deposit_locators import \
    InitialDepositPageLocators


class InitialDepositPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    
    def make_initial_deposit(self):
        time.sleep(10)
        self.click_continue_to_initial_deposit_button()
        self.enter_initial_deposit_amount()
        self.activate_client()
        self.close_app()

    def click_continue_to_initial_deposit_button(self):
        continue_to_initial_deposit_button_locator = InitialDepositPageLocators.CONTINUE_TO_INITIAL_DEPOSIT_BUTTON
        self.wait_and_click_element_by_xpath(continue_to_initial_deposit_button_locator)

    def enter_initial_deposit_amount(self):
        inital_deposit_text_locator = InitialDepositPageLocators.INITIAL_DEPOSIT_TEXT
        deposit_amount = InitialDepositConfig.DEPOSIT_AMOUNT
        self.wait_and_fill_element_using_digits(inital_deposit_text_locator, deposit_amount)

    def activate_client(self):
        get_client_id_api = GetClientIdAPI()
        get_client_id_response = get_client_id_api.get_client_id()
        client_id = get_client_id_response.get('profile_id')
        client_activate_api = ClientActivateAPI(client_id)  
        client_activate_api.client_activate_api()