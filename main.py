# from config import Config , CIVIL_ID_NUMBER, desired_caps
from pages.base_page import BasePage
from tests.get_started_page_tests import test_get_started_page
from tests.initial_deposit_tests import test_initial_deposit_page
from tests.investment_proposal_page_tests import test_investment_proposal_page
from tests.login_page_tests import test_login_page
from tests.personal_info_pages_tests import (test_employment_info_page,
                                             test_personal_info_page,
                                             test_second_personal_info_page,
                                             test_wealth_info_page)
from tests.reopen_app_tests import test_reopen_app
from tests.sign_contract_page_tests import test_contract_page
from tests.upload_id_page_tests import test_upload_id_page
from tests.latest_deposit_page_tests import test_latest_deposit_page
from tests.additional_deposit_tests import test_additional_deposit_page
from tests.withdrawal_tests import test_withdrawal_page
from utils.driver import get_driver, teardown_driver

# Retrieve the driver instance
driver = get_driver()

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