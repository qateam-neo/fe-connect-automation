
import time

from apis.approval import ClientApprovalAPI
from pages.base_page import BasePage
from pages.contract.contract_locators import ContractPageLocators


class ContractPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    
    def sign_contract(self):
        time.sleep(50)
        self.swipe_helper.swipe_from_top_to_bottom()
        self.click_continue_to_contract_button()
        self.select_start_button()
        self.sign_first_page()
        self.select_signature_style()
        self.click_adopt_and_sign()
        self.sign_second_page()
        self.sign_third_page()
        self.sign_fourth_page()
        self.sign_fifth_page()
        self.sign_sixth_page()
        self.sign_last_page()
        self.click_finish_button()
        time.sleep(20)
        self.approve_client()
        self.close_app()
        

    def click_continue_to_contract_button(self):
        continue_to_contract_button_locator = ContractPageLocators.CONTINUE_TO_CONTRACT_BUTTON
        self.wait_and_click_element_by_xpath(continue_to_contract_button_locator)

    def select_start_button(self):
        start_button_locator = ContractPageLocators.START_BUTTON
        self.wait_and_click_element_by_xpath(start_button_locator)

    def sign_first_page(self):
        time.sleep(5)
        sign_first_page_button_locator = ContractPageLocators.SIGN_FIRST_PAGE_BUTTON
        self.wait_and_click_element_by_xpath(sign_first_page_button_locator)

    def select_signature_style(self):
        select_style_button_locator = ContractPageLocators.SELECT_STYLE_BUTTON
        self.wait_and_click_element_by_xpath(select_style_button_locator)

    def click_adopt_and_sign(self):
        self.swipe_helper.swipe_from_top_to_bottom()
        adopt_and_sign_button_locator = ContractPageLocators.ADOPT_AND_SIGN_BUTTON
        self.wait_and_click_element_by_xpath(adopt_and_sign_button_locator)


    def sign_second_page(self):
        sign_second_page_button_locator = ContractPageLocators.SIGN_SECOND_PAGE_BUTTON
        self.wait_and_click_element_by_xpath(sign_second_page_button_locator)

    def sign_third_page(self):
        sign_third_page_button_locator = ContractPageLocators.SIGN_THIRD_PAGE_BUTTON
        self.wait_and_click_element_by_xpath(sign_third_page_button_locator) 

    def sign_fourth_page(self):
        sign_fourth_page_button_locator = ContractPageLocators.SIGN_FOURTH_PAGE_BUTTON
        self.wait_and_click_element_by_xpath(sign_fourth_page_button_locator) 

    def sign_fifth_page(self):
        sign_fifth_page_button_locator = ContractPageLocators.SIGN_FIFTH_PAGE_BUTTON
        self.wait_and_click_element_by_xpath(sign_fifth_page_button_locator) 

    def sign_sixth_page(self):
        sign_sixth_page_button_locator = ContractPageLocators.SIGN_SIXTH_PAGE_BUTTON
        self.wait_and_click_element_by_xpath(sign_sixth_page_button_locator) 

    def sign_last_page(self):
        sign_last_page_button_locator = ContractPageLocators.SIGN_LAST_PAGE_BUTTON
        self.wait_and_click_element_by_xpath(sign_last_page_button_locator) 


    def click_finish_button(self):
        end_of_document_button_locator = ContractPageLocators.END_OF_DOCUMENT_BUTTON
        self.wait_and_click_element_by_xpath(end_of_document_button_locator) 

    def approve_client(self):
        client_apprival = ClientApprovalAPI()
        client_apprival.client_approval_api()
