import time

from pages.base_page import BasePage
from pages.kyc.personal_info.personal_config import PersonalInfo
from pages.kyc.personal_info.personal_info_locators import PersonalnfoLocators


class SecondPersonalInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.swipe_helper.swipe_from_top_to_bottom()
        self.is_nationality_kuwait = PersonalInfo.IS_NATIONALITY_KUWAIT
    
    def fill_second_page_info(self):
        self.click_personal_info_section()

        self.fill_civil_id_serial()
        self.fill_civil_id_expiry_date()

        if not self.is_nationality_kuwait:
            self.fill_passport_number()
            self.choose_passport_country()
            time.sleep(5)
            self.fill_passport_expiry_date()

        self.fill_mother_full_name()
        self.click_contact_address_section()
        self.click_children_number_combo()

        self.swipe_helper.swipe_from_bottom_to_top()
        self.click_personal_info_section_completed()
        self.fill_email()
        self.fill_contact_mobile_number()
        self.click_city_combo()
        self.click_area_combo()
        self.fill_block_field()
        self.fill_street_field()
        self.fill_avenue_field()
        self.fill_house_field()
        self.swipe_helper.swipe_from_bottom_to_top()
        # 
        self.click_contact_address_section2()
        self.swipe_helper.swipe_from_top_to_bottom()
        self.click_continue_button()

    def click_personal_info_section(self):
        personal_info_section_locator = PersonalnfoLocators.PERSONAL_INFORMATION_SECTION
        self.wait_and_click_element_by_xpath(personal_info_section_locator)

    def fill_civil_id_serial(self):
        civil_id_serial_field_locator = PersonalnfoLocators.CIVIL_ID_SERIAL_FIELD
        civil_id_serial =  PersonalInfo.CIVIL_ID_SERIAL
        self.wait_and_fill_input_field_by_xpath(civil_id_serial_field_locator, civil_id_serial)


    def fill_civil_id_expiry_date(self):
        fill_civil_id_expiry_date_field_locator = PersonalnfoLocators.CIVIL_ID_EXPIRY_DATE_FIELD
        civil_id_expiry_date = PersonalInfo.CIVIL_ID_EXPIRY_DATE
        self.wait_and_fill_input_field_by_xpath(fill_civil_id_expiry_date_field_locator, civil_id_expiry_date)
        self.driver.hide_keyboard()

    def fill_mother_full_name(self):
        mother_full_name_field_locator = PersonalnfoLocators.MOTHER_FULL_NAME_FIELD
        mother_full_name = PersonalInfo.MOTHER_FULL_NAME
        self.wait_and_fill_input_field_by_xpath(mother_full_name_field_locator, mother_full_name)


    def click_children_number_combo(self):
        time.sleep(5)
        children_number_combo_locator = PersonalnfoLocators.CHILDREN_NUMBER_COMBO
        self.wait_and_click_element_by_xpath(children_number_combo_locator)
        self.swipe_helper.swipe_from_top_to_bottom()
        children_number_item_locator = PersonalnfoLocators.CHILDREN_NUMBER_ITEM
        self.wait_and_click_element_by_xpath(children_number_item_locator)


    def click_personal_info_section_completed(self):
        time.sleep(5)
        personal_info_section_completed_locator = PersonalnfoLocators.PERSONAL_INFORMATION_SECTION_COMPLETED
        self.wait_and_click_element_by_xpath(personal_info_section_completed_locator)

        
    def click_contact_address_section(self):
        contact_address_section_locator = PersonalnfoLocators.CONTACT_ADDRESS_SECTION
        self.wait_and_click_element_by_xpath(contact_address_section_locator)
    
    def fill_email(self):
        email_text_box_field_locator = PersonalnfoLocators.EMAIL_TEXT_BOX_FIELD
        email_address = PersonalInfo.EMAIL_ADDRESS
        self.wait_and_fill_input_field_by_xpath(email_text_box_field_locator, email_address)
    
    
    def fill_contact_mobile_number(self):
        contact_mobile_number_field_locator = PersonalnfoLocators.CONTACT_MOBILE_NUMBER_FIELD
        contact_mobile_number = PersonalInfo.CONTACT_MOBILE_NUMBER
        self.wait_and_fill_input_field_by_xpath(contact_mobile_number_field_locator, contact_mobile_number)

    def click_city_combo(self):
        time.sleep(3)
        city_combo_locator = PersonalnfoLocators.CITY_COMBO
        self.wait_and_click_element_by_xpath(city_combo_locator)
        time.sleep(1)
        city_item_locator = PersonalnfoLocators.CITY_ITEM

        self.wait_and_click_element_by_xpath(city_item_locator) 
        


    def click_area_combo(self):
        self.swipe_helper.swipe_from_top_to_bottom()
        area_combo_locator = PersonalnfoLocators.AREA_COMBO
        self.wait_and_click_element_by_xpath(area_combo_locator)
        # time.sleep(5)
        # self.driver.hide_keyboard()
        area_combo_item_locator = PersonalnfoLocators.AREA_COMBO_ITEM
        self.wait_and_click_element_by_xpath(area_combo_item_locator)

    def fill_block_field(self):
        block_text_box_field_locator = PersonalnfoLocators.ADDRESS_BLOCK_FIELD
        block = PersonalInfo.ADDRESS_BLOCK_FIELD
        self.wait_and_fill_input_field_by_xpath(block_text_box_field_locator, block)

    def fill_street_field(self):
        street_text_box_field_locator = PersonalnfoLocators.STREET_FIELD
        street = PersonalInfo.STREET_FIELD
        self.wait_and_fill_input_field_by_xpath(street_text_box_field_locator, street)

    def fill_avenue_field(self):
        avenue_text_box_field_locator = PersonalnfoLocators.AVENUE_FIELD
        avenue = PersonalInfo.AVENUE_FIELD
        self.wait_and_fill_input_field_by_xpath(avenue_text_box_field_locator, avenue)

    def fill_house_field(self):
        house_text_box_field_locator = PersonalnfoLocators.HOUSE_FIELD
        house = PersonalInfo.HOUSE_FIELD
        self.wait_and_fill_input_field_by_xpath(house_text_box_field_locator, house)


    def click_contact_address_section2(self):
        contact_address_section2_locator = PersonalnfoLocators.CONTACT_ADDRESS_SECTION2
        self.wait_and_click_element_by_xpath(contact_address_section2_locator)

    def click_continue_button(self):
        time.sleep(1)
        continue_button_locator = PersonalnfoLocators.CONTINUE_BUTTON_SECOND_INFO_PAGE1
        self.wait_and_click_element_by_xpath(continue_button_locator)
        time.sleep(1)

    def fill_passport_number(self):
        passport_number_text_box_locator = PersonalnfoLocators.PASSPORT_NUMBER_FIELD
        passport_number_text = PersonalInfo.PASSPORT_NUMBER
        self.wait_and_fill_input_field_by_xpath(passport_number_text_box_locator, passport_number_text)

    def choose_passport_country(self):
        time.sleep(5)
        passport_country_locator = PersonalnfoLocators.PASSPORT_COUNTRY_COMBO
        self.wait_and_click_element_by_xpath(passport_country_locator)

        passport_item_locator = PersonalnfoLocators.PASSPORT_COUNTRY_ITEM
        self.wait_and_click_element_by_xpath(passport_item_locator)

    def fill_passport_expiry_date(self):
        passport_expiry_date_text_box_locator = PersonalnfoLocators.PASSPORT_EXPIRY_DATE_FIELD
        passport_expiry_date = PersonalInfo.PASSPORT_EXPIRY_DATE
        self.wait_and_fill_input_field_by_xpath(passport_expiry_date_text_box_locator, passport_expiry_date)
        self.driver.hide_keyboard()