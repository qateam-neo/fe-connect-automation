
from pages.active_dashboard.additional_deposit.additional_deposit import AdditionalDepositPage

# Define the test case
def test_additional_deposit_page(driver):
    additional_deposit_page = AdditionalDepositPage(driver)
    additional_deposit_page.make_additional_deposit()
