from appium.webdriver.webdriver import WebDriver
from config import Config 


_driver = None

def get_driver():
    global _driver
    if _driver is None:
        try:
           _driver = WebDriver(Config.APPIUM_SERVER_URL, Config.desired_caps)
        except:
            Config.desired_caps['sessionId'] = _driver.session_id
            _driver = WebDriver.Remote(Config.APPIUM_SERVER_URL, Config.desired_caps)
        session_id = _driver.session_id
        print('driver', _driver)
        print('session id', session_id)
    return _driver


def teardown_driver():
    global _driver
    if _driver is not None:
        _driver.quit()
        _driver = None
        