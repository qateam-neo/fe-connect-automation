import time
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from pages.kyc.employment_info.employment_info_page_config import EmploymentInfoPageConfig
from pages.kyc.employment_info.employment_info_page_locators import EmploymentInfoPageIDs
from pages.kyc.personal_info.personal_info_second_page.main import PersonalInfoSecondScreen

class EmploymentInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def start(self):
        time.sleep(1)
        if not self.is_element_visible(EmploymentInfoPageIDs.SCREEN_TRIGGER_IDENTIFICATION,10):
            print("ERROR: TIMEOUT screen employment not shown")
        # time.sleep(20)
        self.click_employment_section()
        self.select_employment_status()
        # self.select_board_membership()
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
        self.click_hidden_element(EmploymentInfoPageIDs.EMPLOYMENT_SECTION)
        # PersonalInfoSecondScreen(self.driver).start()

        
        
    def select_employment_status(self):

        self.click_hidden_element(EmploymentInfoPageIDs.EMPLOYMENT_COMBO)
        time.sleep(0.5)
        self.click_hidden_element(EmploymentInfoPageIDs.EMPLOYMENT_ITEM)
        
    def select_board_membership(self):
        self.click_hidden_element(EmploymentInfoPageIDs.BOARD_MEMBERSHIP_SWITCH_BUTTON)

    def close_employment_section(self):
        self.click_hidden_element(EmploymentInfoPageIDs.EMPLOYMENT_SECTION_COMPLETED)

    def select_income_information_section(self):
        self.click_hidden_element(EmploymentInfoPageIDs.INCOME_INFORMATION_SECTION)

    def select_primary_objective(self):

        self.click_hidden_element(EmploymentInfoPageIDs.PRIMARY_OBJECTIVE_COMBO)
        time.sleep(0.5)
        self.click_hidden_element(EmploymentInfoPageIDs.PRIMARY_OBJECTIVE_ITEM)

    def select_annual_income(self):
        
        self.click_hidden_element(EmploymentInfoPageIDs.ANNUAL_INCOME_COMBO)
        time.sleep(0.5)
        self.click_hidden_element(EmploymentInfoPageIDs.ANNUAL_INCOME_ITEM)
    
    def select_source_of_income(self):
        self.click_hidden_element(EmploymentInfoPageIDs.SOURCE_OF_INCOME_COMBO)
        time.sleep(0.5)
        self.click_hidden_element(EmploymentInfoPageIDs.SOURCE_OF_INCOME_ITEM)

    def fill_details_of_income(self):
        
        bottom=self.get_hidden_element(EmploymentInfoPageIDs.TOTAL_VALUE_COMBO)
        bottomY=bottom.location["y"]
        
        top=self.get_hidden_element(EmploymentInfoPageIDs.DETAILS_OF_INCOME_TOP)
        topY=top.location["y"]
        
        x_coordinates_details=top.location["x"]+100
        y_coordinates_details=(bottomY-(bottomY-topY)/2)+40
        
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(None, x_coordinates_details, y_coordinates_details).click().perform()
        action.send_keys("Details of income").perform()

        # self.send_keys(element=EmploymentInfoPageIDs.DETAILS_OF_INCOME_TEXT,
        #            value=EmploymentInfoPageConfig.DETAILS_OF_SOURCE_INCOME)

    def select_total_value(self):     
        self.click_hidden_element(EmploymentInfoPageIDs.TOTAL_VALUE_COMBO)
        time.sleep(0.5)
        self.click_hidden_element(EmploymentInfoPageIDs.TOTAL_VALUE_ITEM)

    def select_value_of_transactions(self):   
        self.click_hidden_element(EmploymentInfoPageIDs.VALUE_OF_TRANSACTIONS_COMBO)
        time.sleep(0.5)
        self.click_hidden_element(EmploymentInfoPageIDs.VALUE_OF_TRANSACTIONS_ITEM)

    def select_value_of_assets(self):
        self.click_hidden_element(EmploymentInfoPageIDs.VALUE_OF_ASSETS_COMBO)
        time.sleep(0.5)
        self.click_hidden_element(EmploymentInfoPageIDs.VALUE_OF_ASSETS_ITEM)
        
    def select_years_worked_in_financial_sector(self):
        self.click_hidden_element(EmploymentInfoPageIDs.YEARS_WORKED_IN_FINANCIAL_SECTOR_COMBO)
        time.sleep(0.5)
        self.click_hidden_element(EmploymentInfoPageIDs.YEARS_WORKED_IN_FINANCIAL_SECTOR_ITEM)

    def click_continue_button(self):
        self.click_hidden_element(EmploymentInfoPageIDs.CONTINUE_BUTTON_OLD)
        time.sleep(1)