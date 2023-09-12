# from config import Config , CIVIL_ID_NUMBER, desired_caps
import os,sys

from pages.get_started.main import GetStartedPage
from pages.investment_proposal.historical_performance.main import HistoricalPerformanceFlow
from pages.investment_proposal.main import OnboardingFlow
from pages.kyc.personal_info.main import PersonalInfoFullFlow

from pages.login.main import LoginPage
from utils.driver import AppiumDriver
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.append(os.getcwd())
from pages.base_page import BasePage

from tests.initial_deposit_tests import test_initial_deposit_page

from tests.personal_info_pages_tests import (test_employment_info_page,
                                             test_wealth_info_page)
from tests.reopen_app_tests import test_reopen_app
from tests.sign_contract_page_tests import test_contract_page
from tests.upload_id_page_tests import test_upload_id_page
from tests.latest_deposit_page_tests import test_latest_deposit_page
from tests.additional_deposit_tests import test_additional_deposit_page
from tests.withdrawal_tests import test_withdrawal_page


# Retrieve the driver instance
driver = AppiumDriver().get_driver()

# Define a main function to run all tests   
def run_basic_smoke_test():
    BasePage(driver)
    test_login_page(driver)
    test_get_started_page(driver)
    test_investment_proposal_page(driver)
    test_personal_info_page(driver)
    test_second_personal_info_page(driver)
    test_employment_info_page(driver)
    test_wealth_info_page(driver)
    test_upload_id_page(driver)
    test_contract_page(driver)
    test_reopen_app(driver)
    test_initial_deposit_page(driver)
    test_login_page(driver)
    test_additional_deposit_page(driver)
    test_latest_deposit_page(driver)
    test_login_page(driver)
    test_withdrawal_page(driver)

    
# Call the main function to run smoke test (run all tests)
run_basic_smoke_test()

# teardown_driver()
teardown_driver()