
from tests.login_page_tests import test_login_page


def test_reopen_app(driver):
    test_login_page(driver)