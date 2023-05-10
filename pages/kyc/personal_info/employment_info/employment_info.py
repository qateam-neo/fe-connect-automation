import time

from pages.base_page import BasePage
from pages.kyc.personal_info.employment_info.employment_info_page_locators import \
    EmploymentInfoPageLocators
from pages.kyc.personal_info.employment_info.employment_info_page_config import \
    EmploymentInfoPageConfig

class EmploymentInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_employment_page_info(self):
        time.sleep(1)
        time.sleep(20)
        self.click_employment_section()
        self.select_employment_status()
        self.select_board_membership()
        self.close_employment_section()
        self.select_income_information_section()
        self.select_primary_objective()
        self.select_annual_income()
        self.swipe_helper.swipe_from_top_to_bottom()
        self.select_source_of_income()
        time.sleep(5)
        self.fill_details_of_income()
        
        time.sleep(1)
        # self.swipe_helper.swipe_from_top_to_bottom()
        self.select_total_value()
        self.select_value_of_transactions()
        self.select_value_of_assets()
        self.select_years_worked_in_financial_sector()
        self.swipe_helper.swipe_from_bottom_to_top()
        self.select_income_information_section()
        self.click_continue_button()
        

        
    def click_employment_section(self):
        employment_section_locator = EmploymentInfoPageLocators.EMPLOYMENT_SECTION_COMPLETED
        self.wait_and_click_element_by_xpath(employment_section_locator)

    def select_employment_status(self):
        employment_status_combo = EmploymentInfoPageLocators.EMPLOYMENT_COMBO
        self.wait_and_click_element_by_xpath(employment_status_combo)

        employment_status_item = EmploymentInfoPageLocators.EMPLOYMENT_ITEM
        self.wait_and_click_element_by_xpath(employment_status_item)

    def select_board_membership(self):
        membership_locator = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[1]/android.view.View[2]'
        self.wait_and_click_element_by_xpath(membership_locator)

    def close_employment_section(self):
        employment_section_locator = EmploymentInfoPageLocators.EMPLOYMENT_SECTION_COMPLETED
        self.wait_and_click_element_by_xpath(employment_section_locator)

    def select_income_information_section(self):
        income_information_section_locator = EmploymentInfoPageLocators.INCOME_INFORMATION_SECTION
        self.wait_and_click_element_by_xpath(income_information_section_locator)

    def select_primary_objective(self):
        primary_objective_combo = EmploymentInfoPageLocators.PRIMARY_OBJECTIVE_COMBO
        self.wait_and_click_element_by_xpath(primary_objective_combo)

        primary_objective_item = EmploymentInfoPageLocators.PRIMARY_OBJECTIVE_ITEM
        self.wait_and_click_element_by_xpath(primary_objective_item)

    def select_annual_income(self):
        annual_income_combo = EmploymentInfoPageLocators.ANNUAL_INCOME_COMBO
        self.wait_and_click_element_by_xpath(annual_income_combo)

        annual_income_item = EmploymentInfoPageLocators.ANNUAL_INCOME_ITEM
        self.wait_and_click_element_by_xpath(annual_income_item)
    
    def select_source_of_income(self):
        source_of_income_combo = EmploymentInfoPageLocators.SOURCE_OF_INCOME_COMBO
        self.wait_and_click_element_by_xpath(source_of_income_combo)

        source_of_income_item = EmploymentInfoPageLocators.SOURCE_OF_INCOME_ITEM
        self.wait_and_click_element_by_xpath(source_of_income_item)


    def fill_details_of_income(self):
        source_income_details_locator = EmploymentInfoPageLocators.DETAILS_OF_INCOME_TEXT
        source_of_income_details_value = EmploymentInfoPageConfig.DETAILS_OF_SOURCE_INCOME

        print(source_of_income_details_value)
        self.wait_and_fill_input_field_by_xpath(source_income_details_locator, source_of_income_details_value)


    def select_total_value(self):
        total_value_combo = EmploymentInfoPageLocators.TOTAL_VALUE_COMBO
        self.wait_and_click_element_by_xpath(total_value_combo)

        total_value_item = EmploymentInfoPageLocators.TOTAL_VALUE_ITEM
        self.wait_and_click_element_by_xpath(total_value_item)

    def select_value_of_transactions(self):
        value_of_transactions_combo = EmploymentInfoPageLocators.VALUE_OF_TRANSACTIONS_COMBO
        self.wait_and_click_element_by_xpath(value_of_transactions_combo)

        value_of_transactions_item = EmploymentInfoPageLocators.VALUE_OF_TRANSACTIONS_ITEM
        self.wait_and_click_element_by_xpath(value_of_transactions_item)
        
    def select_value_of_assets(self):
        value_of_assets_combo = EmploymentInfoPageLocators.VALUE_OF_ASSETS_COMBO
        self.wait_and_click_element_by_xpath(value_of_assets_combo)

        value_of_assets_item = EmploymentInfoPageLocators.VALUE_OF_ASSETS_ITEM
        self.wait_and_click_element_by_xpath(value_of_assets_item)
        

    def select_years_worked_in_financial_sector(self):
        years_worked_in_financial_sector_combo = EmploymentInfoPageLocators.YEARS_WORKED_IN_FINANCIAL_SECTOR_COMBO
        self.wait_and_click_element_by_xpath(years_worked_in_financial_sector_combo)

        years_worked_in_financial_sector_item = EmploymentInfoPageLocators.YEARS_WORKED_IN_FINANCIAL_SECTOR_ITEM
        self.wait_and_click_element_by_xpath(years_worked_in_financial_sector_item)


    def click_continue_button(self):
        continue_button_locator = EmploymentInfoPageLocators.CONTINUE_BUTTON_OLD
        self.wait_and_click_element_by_xpath(continue_button_locator)
        time.sleep(1)