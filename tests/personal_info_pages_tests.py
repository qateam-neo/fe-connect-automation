from pages.kyc.personal_info.personal_info import PersonalInfoPage
from pages.kyc.personal_info.second_personal_info import SecondPersonalInfoPage
from pages.kyc.personal_info.employment_info.employment_info import EmploymentInfoPage
from pages.kyc.personal_info.wealth_info.wealth_info import WealthInfoPage

# Define the test case
def test_personal_info_page(driver):
    personal_info_page = PersonalInfoPage(driver)
    personal_info_page.fill_first_personal_info_page()

def test_second_personal_info_page(driver):
    second_personal_info_page = SecondPersonalInfoPage(driver)
    second_personal_info_page.fill_second_page_info()

def test_employment_info_page(driver):
    third_personal_info_page = EmploymentInfoPage(driver)
    third_personal_info_page.fill_employment_page_info()

def test_wealth_info_page(driver):
    third_personal_info_page = WealthInfoPage(driver)
    third_personal_info_page.fill_wealth_page_info()