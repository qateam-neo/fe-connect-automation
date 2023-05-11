from pages.initial_deposit.initial_deposit import InitialDepositPage

def test_initial_deposit_page(driver):
    initial_deposit_page = InitialDepositPage(driver)
    initial_deposit_page.make_initial_deposit()