import time

from pages.base_page import BasePage
from pages.kyc.wealth_info.wealth_info_config import WealthInfo
from pages.kyc.wealth_info.wealth_info_page_locators import WealthInfoPageLocators



class WealthInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_wealth_page_info(self):
        self.click_wealth_info_section()
        self.select_purpose_of_opening_account()
        self.select_level_of_investment_knowledge()
        self.select_years_of_investment_experience()
        self.select_risk_of_tolerance()
        self.fill_wealth_amount()
        time.sleep(1)
        self.swipe_helper.swipe_from_top_to_bottom()
        self.select_source_of_wealth()
        self.fill_wealth_details()
        self.click_continue_button()


    def click_wealth_info_section(self):
        wealth_info_section_locator = WealthInfoPageLocators.WEALTH_INFORMATION_SECTION
        self.wait_and_click_element_by_xpath(wealth_info_section_locator)

    def select_purpose_of_opening_account(self):
        purpose_combo = WealthInfoPageLocators.PURPOSE_COMBO
        self.wait_and_click_element_by_xpath(purpose_combo)

        purpose_item = WealthInfoPageLocators.PURPOSE_ITEM
        self.wait_and_click_element_by_xpath(purpose_item)


    def select_level_of_investment_knowledge(self):
        level_of_investment_knowledge_locator = WealthInfoPageLocators.LEVEL_OF_INVESTMENT_KNOWLEDGE_COMBO
        self.wait_and_click_element_by_xpath(level_of_investment_knowledge_locator)
        level_of_investment_knowledge_item = WealthInfoPageLocators.LEVEL_OF_INVESTMENT_KNOWLEDGE_ITEM
        self.wait_and_click_element_by_xpath(level_of_investment_knowledge_item)

    def select_years_of_investment_experience(self):
        investment_experience_combo_locator = WealthInfoPageLocators.INVESTMENT_EXPERIENCE_COMBO
        self.wait_and_click_element_by_xpath(investment_experience_combo_locator)

        investment_experience_item_locator = WealthInfoPageLocators.INVESTMENT_EXPERIENCE_ITEM
        self.wait_and_click_element_by_xpath(investment_experience_item_locator)

    def select_risk_of_tolerance(self):
        risk_of_tolerance_combo_locator = WealthInfoPageLocators.RISK_TOLERANCE_COMBO
        self.wait_and_click_element_by_xpath(risk_of_tolerance_combo_locator)

        risk_of_tolerance_item_locator = WealthInfoPageLocators.RISK_TOLERANCE_ITEM
        self.wait_and_click_element_by_xpath(risk_of_tolerance_item_locator)

    def fill_wealth_amount(self):
        time.sleep(1)
        wealth_amount_textbox_locator = WealthInfoPageLocators.WEALTH_AMOUNT_TEXT
        wealth_amount = WealthInfo.WEALTH_AMOUNT
        self.wait_scroll_vertically_to_element_by_xpath_and_fill_using_digits(wealth_amount_textbox_locator, wealth_amount)
        time.sleep(1)
        
    def select_source_of_wealth(self):
        source_of_wealth_combo_locator = WealthInfoPageLocators.SOURCE_OF_WEALTH_COMBO
        self.wait_and_click_element_by_xpath(source_of_wealth_combo_locator)

        source_of_wealth_item_locator = WealthInfoPageLocators.SOURCE_OF_WEALTH_ITEM
        self.wait_and_click_element_by_xpath(source_of_wealth_item_locator)


    def fill_wealth_details(self):
        wealth_details_textbox_locator = WealthInfoPageLocators.WEALTH_DETAILS_TEXT
        wealth_details = WealthInfo.WEALTH_DETAILS_TEXT
        self.wait_and_fill_input_field_by_xpath(wealth_details_textbox_locator, wealth_details)

    def click_continue_button(self):
        continue_button_locator = WealthInfoPageLocators.CONTINUE_BUTTON
        self.wait_and_click_element_by_xpath(continue_button_locator)