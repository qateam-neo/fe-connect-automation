from pages.login.login import LoginPage

# Define the test case
def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.login()



