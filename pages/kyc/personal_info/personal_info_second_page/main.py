import time

from pages.base_page import BasePage
from pages.kyc.personal_info.config import PersonalInfo
from pages.kyc.personal_info.personal_info_second_page.config import ELEMENTS



class PersonalInfoSecondScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.swipe_helper.swipe_from_top_to_bottom()
        self.is_nationality_kuwait = PersonalInfo.IS_NATIONALITY_KUWAIT
    
    def start(self):
        self.click_personal_info_section()
        self.fill_civil_id_serial()
        self.fill_civil_id_expiry_date()

        if not self.is_nationality_kuwait:
            self.fill_passport_number()
            self.choose_passport_country()
            time.sleep(5)
            self.fill_passport_expiry_date()

        self.fill_mother_full_name()
        self.click_contact_info_section()
        self.click_children_number_combo()

        # self.swipe_helper.swipe_from_top_to_bottom()
        self.fill_email()
        self.fill_confirm_email()
        self.fill_contact_mobile_number()
        self.click_city_combo()
        self.click_area_combo()
        self.fill_block_field()
        self.fill_street_field()
        self.fill_avenue_field()
        self.fill_house_field()
        # self.swipe_helper.swipe_from_bottom_to_top()
        # # 
        # self.click_contact_address_section2()
        self.swipe_helper.swipe_from_top_to_bottom()
        self.click_continue_button()

    def click_personal_info_section(self):
        iteration=1
        while not self.wait_and_get_element_by_text("Enter First name, Middle name, and Last name in full"):
            if iteration>2:
                self.wait_and_get_element_by_text("dropdown-arrow").click()

            self.click_element(ELEMENTS.PERSONAL_INFORMATION_SECTION,1)
            iteration=iteration+1


    def fill_civil_id_serial(self):
        self.send_keys(ELEMENTS.CIVIL_ID_SERIAL_FIELD,PersonalInfo.CIVIL_ID_SERIAL,2)


    def fill_civil_id_expiry_date(self):
        self.send_keys(ELEMENTS.CIVIL_ID_EXPIRY_DATE_FIELD,PersonalInfo.CIVIL_ID_EXPIRY_DATE,2)
        self.driver.hide_keyboard()

    def fill_mother_full_name(self):
        self.send_keys(ELEMENTS.MOTHER_FULL_NAME_FIELD,PersonalInfo.MOTHER_FULL_NAME,2)

    def click_children_number_combo(self):
        time.sleep(2) 
        self.swipe_helper.swipe_from_top_to_bottom()
        self.click_element(ELEMENTS.CHILDREN_NUMBER_COMBO)
        self.click_element(ELEMENTS.CHILDREN_NUMBER_ITEM)


    def click_contact_info_section(self):
        time.sleep(3)
        self.click_element(ELEMENTS.CONTACT_INFORMATION_SECTION)

    
    def fill_email(self):
        self.send_keys(ELEMENTS.EMAIL_TEXT_BOX_FIELD,PersonalInfo.EMAIL_ADDRESS)
    
    def fill_confirm_email(self):
        self.send_keys(ELEMENTS.CONFIRM_EMAIL_TEXT_BOX_FIELD,PersonalInfo.EMAIL_ADDRESS)
    
    def fill_contact_mobile_number(self):
        self.send_keys(ELEMENTS.CONTACT_MOBILE_NUMBER_FIELD,PersonalInfo.CONTACT_MOBILE_NUMBER)

    def click_city_combo(self):
        self.driver.hide_keyboard()

        time.sleep(3)
        self.click_element(ELEMENTS.CITY_COMBO)
        self.driver.hide_keyboard()
        time.sleep(2)
        self.click_hidden_element(ELEMENTS.CITY_ITEM,top_to_bottom=True) 
        


    def click_area_combo(self):

        self.swipe_helper.swipe_from_top_to_bottom()
        time.sleep(2)
        self.driver.hide_keyboard()
        self.click_hidden_element(ELEMENTS.AREA_COMBO,top_to_bottom=False)
        self.driver.hide_keyboard()

        # self.swipe_helper.swipe_from_top_to_bottom(scale=0.6)
        time.sleep(2)
        self.driver.hide_keyboard()

        self.click_hidden_element(ELEMENTS.AREA_COMBO_ITEM)

    def fill_block_field(self):
        self.swipe_helper.swipe_from_top_to_bottom()
        self.send_keys(ELEMENTS.ADDRESS_BLOCK_FIELD,PersonalInfo.ADDRESS_BLOCK_FIELD,hidden=True,top_to_bottom=False)

    def fill_street_field(self):
        self.send_keys(ELEMENTS.STREET_FIELD,PersonalInfo.STREET_FIELD,hidden=True,top_to_bottom=False)
        self.driver.hide_keyboard()

    def fill_avenue_field(self):
        self.send_keys(ELEMENTS.AVENUE_FIELD,PersonalInfo.AVENUE_FIELD,hidden=True,top_to_bottom=False)
        self.driver.hide_keyboard()

    def fill_house_field(self):
        self.send_keys(ELEMENTS.HOUSE_FIELD,PersonalInfo.HOUSE_FIELD,hidden=True,top_to_bottom=False)
        self.driver.hide_keyboard()

    def click_contact_address_section2(self):
        self.click_element(ELEMENTS.CONTACT_ADDRESS_SECTION2)

    def click_continue_button(self):
        
        time.sleep(1)
        self.click_hidden_element(ELEMENTS.CONTINUE_BUTTON_SECOND_INFO_PAGE1,top_to_bottom=False)
        time.sleep(1)

    def fill_passport_number(self):
        passport_number_text_box_locator = ELEMENTS.PASSPORT_NUMBER_FIELD
        passport_number_text = PersonalInfo.PASSPORT_NUMBER
        self.wait_and_fill_input_field_by_xpath(passport_number_text_box_locator, passport_number_text)

    def choose_passport_country(self):
        time.sleep(5)
        passport_country_locator = ELEMENTS.PASSPORT_COUNTRY_COMBO
        self.wait_and_click_element_by_xpath(passport_country_locator)

        passport_item_locator = ELEMENTS.PASSPORT_COUNTRY_ITEM
        self.wait_and_click_element_by_xpath(passport_item_locator)

    def fill_passport_expiry_date(self):
        passport_expiry_date_text_box_locator = ELEMENTS.PASSPORT_EXPIRY_DATE_FIELD
        passport_expiry_date = PersonalInfo.PASSPORT_EXPIRY_DATE
        self.wait_and_fill_input_field_by_xpath(passport_expiry_date_text_box_locator, passport_expiry_date)
        self.driver.hide_keyboard()