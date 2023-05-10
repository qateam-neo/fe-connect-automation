from pages.base_page import BasePage
from pages.kyc.personal_info.personal_config import PersonalInfo
from pages.kyc.personal_info.personal_info_locators import PersonalnfoLocators
import time

class PersonalInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.swipe_helper.swipe_from_top_to_bottom()
        self.edit_kyc_name = PersonalInfo.EDIT_KYC_NAME
        self.is_nationality_kuwait = PersonalInfo.IS_NATIONALITY_KUWAIT

    def fill_first_personal_info_page(self):
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
        self.swipe_helper.swipe_from_top_to_bottom()
        change_my_name_button_xpath = PersonalnfoLocators.CHANGE_MY_NAME_BUTTON_XPATH
        self.wait_and_click_element_by_xpath(change_my_name_button_xpath)

    def fill_first_name(self):
        first_name = PersonalInfo.FIRST_NAME
        self.wait_and_fill_input_field_by_xpath(PersonalnfoLocators.FIRST_NAME_FIELD, first_name)

    def fill_middle_name(self):
        middle_name = PersonalInfo.MIDDLE_NAME
        self.wait_and_fill_input_field_by_xpath(PersonalnfoLocators.MIDDLE_NAME_FIELD, middle_name)

    def fill_last_name(self):
        last_name = PersonalInfo.LAST_NAME
        self.wait_and_fill_input_field_by_xpath(PersonalnfoLocators.LAST_NAME_FIELD, last_name)

    def click_change_my_name_continue_button(self):
        change_my_name_continue_button = PersonalnfoLocators.CHANGE_MY_NAME_CONTINUE_BUTTON
        self.wait_and_click_element_by_xpath(change_my_name_continue_button)


    def click_continue_button_to_fill_name_page(self):
        self.swipe_helper.swipe_from_top_to_bottom()
        continue_button_to_fill_name_page = PersonalnfoLocators.CONTINUE_BUTTON_TO_FILL_NAME_PAGE
        self.wait_and_click_element_by_xpath(continue_button_to_fill_name_page)

    def choose_first_name(self):

        first_name_combo = PersonalnfoLocators.FIRST_NAME_COMBO
        self.wait_and_click_element_by_xpath(first_name_combo)

        first_name_item = PersonalnfoLocators.FIRST_NAME_ITEM
        self.wait_and_click_element_by_xpath(first_name_item)

    def choose_last_name(self):
        
        last_name_combo = PersonalnfoLocators.LAST_NAME_COMBO
        print(last_name_combo)
        self.wait_and_click_element_by_xpath(last_name_combo)

        last_name_item = PersonalnfoLocators.LAST_NAME_ITEM
        print(last_name_item)
        self.wait_and_click_element_by_xpath(last_name_item)



    def click_change_name_page_continue_button(self):
        change_name_page_continue_button = PersonalnfoLocators.CHOOSE_NAME_PAGE_CONTINUE_BUTTON
        self.wait_and_click_element_by_xpath(change_name_page_continue_button)



    def choose_middle_name(self):
        middle_name_locator = PersonalnfoLocators.MIDDLE_NAME_FIELD
        middle_name_value = PersonalInfo.MIDDLE_NAME
        self.wait_and_fill_input_field_by_xpath(middle_name_locator, middle_name_value)


    def click_change_middle_name_page_continue_button(self):
        change_middle_name_page_continue_button = PersonalnfoLocators.CHOOSE_MIDDLE_NAME_PAGE_CONTINUE_BUTTON
        self.wait_and_click_element_by_xpath(change_middle_name_page_continue_button)        

    def choose_nationality(self):
        time.sleep(5)
        nationality_combo = PersonalnfoLocators.NATIONALITY_COMBO
        print(nationality_combo)
        self.wait_and_click_element_by_xpath(nationality_combo)
        nationality_item = PersonalnfoLocators.NATIONALITY_ITEM
        print(nationality_item)
        self.wait_and_click_element_by_xpath(nationality_item)  


  
        