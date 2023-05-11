
from pages.active_dashboard.withdrawal.withdrawal import WithdrawalPage

# Define the test case
def test_withdrawal_page(driver):
    latest_deposit_page = WithdrawalPage(driver)
    latest_deposit_page.make_withdrawal()
