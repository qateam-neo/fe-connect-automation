from pages.base_page import BasePage

import time

from pages.kyc.personal_info.config import PersonalInfo
from pages.kyc.personal_info.personal_info_first_page.config import ELEMENTS

class PersonalInfoFirstScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.swipe_helper.swipe_from_top_to_bottom()
        self.edit_kyc_name = PersonalInfo.EDIT_KYC_NAME
        self.is_nationality_kuwait = PersonalInfo.IS_NATIONALITY_KUWAIT

    def start(self):
        if not self.is_nationality_kuwait:
            self.choose_nationality()
        
        if self.edit_kyc_name:
            self.click_change_my_name()
            self.fill_first_name()
            self.fill_middle_name()
            self.fill_last_name()
            self.click_change_my_name_continue_button()
        else:   
            self.click_continue_button_to_fill_name_page()           
            self.choose_first_name()
            self.choose_last_name()
            self.click_change_name_page_continue_button()

            self.choose_middle_name()
            self.click_change_middle_name_page_continue_button()
            print('fill name')

        
        
    def click_change_my_name(self):
        if self.wait_and_get_element_by_text("Kindly review and confirm"):
            self.swipe_helper.swipe_from_top_to_bottom()
        while not self.wait_and_get_element_by_text("full name as indicated"):
            self.click_hidden_element(ELEMENTS.CHANGE_MY_NAME_BUTTON)
        
    def fill_first_name(self):
        self.send_keys(ELEMENTS.FIRST_NAME_FIELD,PersonalInfo.FIRST_NAME,5)

    def fill_middle_name(self):
        self.send_keys(ELEMENTS.MIDDLE_NAME_FIELD,PersonalInfo.MIDDLE_NAME)

    def fill_last_name(self):
        self.send_keys(ELEMENTS.LAST_NAME_FIELD,PersonalInfo.LAST_NAME)

    def click_change_my_name_continue_button(self):
        self.click_element(ELEMENTS.CHANGE_MY_NAME_CONTINUE_BUTTON)


    def click_continue_button_to_fill_name_page(self):
        self.swipe_helper.swipe_from_top_to_bottom()
        continue_button_to_fill_name_page = ELEMENTS.CONTINUE_BUTTON_TO_FILL_NAME_PAGE
        self.wait_and_click_element_by_xpath(continue_button_to_fill_name_page)

    def choose_first_name(self):

        first_name_combo = ELEMENTS.FIRST_NAME_COMBO
        self.wait_and_click_element_by_xpath(first_name_combo)

        first_name_item = ELEMENTS.FIRST_NAME_ITEM
        self.wait_and_click_element_by_xpath(first_name_item)

    def choose_last_name(self):
        
        last_name_combo = ELEMENTS.LAST_NAME_COMBO
        print(last_name_combo)
        self.wait_and_click_element_by_xpath(last_name_combo)

        last_name_item = ELEMENTS.LAST_NAME_ITEM
        print(last_name_item)
        self.wait_and_click_element_by_xpath(last_name_item)



    def click_change_name_page_continue_button(self):
        change_name_page_continue_button = ELEMENTS.CHOOSE_NAME_PAGE_CONTINUE_BUTTON
        self.wait_and_click_element_by_xpath(change_name_page_continue_button)



    def choose_middle_name(self):
        middle_name_locator = ELEMENTS.MIDDLE_NAME_FIELD
        middle_name_value = PersonalInfo.MIDDLE_NAME
        self.wait_and_fill_input_field_by_xpath(middle_name_locator, middle_name_value)


    def click_change_middle_name_page_continue_button(self):
        change_middle_name_page_continue_button = ELEMENTS.CHOOSE_MIDDLE_NAME_PAGE_CONTINUE_BUTTON
        self.wait_and_click_element_by_xpath(change_middle_name_page_continue_button)        

    def choose_nationality(self):
        time.sleep(5)
        nationality_combo = ELEMENTS.NATIONALITY_COMBO
        print(nationality_combo)
        self.wait_and_click_element_by_xpath(nationality_combo)
        nationality_item = ELEMENTS.NATIONALITY_ITEM
        print(nationality_item)
        self.wait_and_click_element_by_xpath(nationality_item)  


  
        