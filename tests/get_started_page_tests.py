
from pages.get_started.get_started import GetStartedPage

# Define the test case
def test_get_started_page(driver):
    get_started_page = GetStartedPage(driver)
    get_started_page.click_get_started_button()
