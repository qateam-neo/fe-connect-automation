
from pages.contract.contract import ContractPage

# Define the test case
def test_contract_page(driver):
    contract_page = ContractPage(driver)
    contract_page.sign_contract()