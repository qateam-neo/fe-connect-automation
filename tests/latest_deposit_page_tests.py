
from pages.latest_deposit.latest_deposit import LatestDepositPage

# Define the test case
def test_latest_deposit_page(driver):
    latest_deposit_page = LatestDepositPage(driver)
    latest_deposit_page.submit_latest_deposit()
