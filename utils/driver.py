from appium.webdriver.webdriver import WebDriver
from config import Config 
from appium import webdriver

_driver = None
class AppiumDriver:
    def __init__(self) -> None:
        self.desired_caps = {
                "deviceName": "Android Emulator",
                "platformName": "Android",
                "udid":"emulator-5554",
                "version" : "13",
                "app": "/Users/mohamadharb/Downloads/PJ-Connect.apk",
                # "appPackage": "neo.nbkc.smartwealth.demo",
                # "appActivity":"com.nbkcapitalsmartwealth.app.splash.SplashActivity",
                "newCommandTimeout":120	,
                "autoGrantPermissions" : "true"}
        self.desired_caps_no_app = {
                        "deviceName": "Android Emulator",
                        "platformName": "Android",
                        "udid":"emulator-5554",
                        "version" : "13",
                        "newCommandTimeout":120	,
                        "autoGrantPermissions" : "true"}
            

    def get_driver(self):
        global _driver
        if _driver is None:
            try:
            #    _driver = WebDriver(Config.APPIUM_SERVER_URL, self.desired_caps)
                _driver = webdriver.Remote(Config.APPIUM_SERVER_URL, self.desired_caps)

            except Exception as e:
                print(e)
                Config.self.desired_caps['sessionId'] = _driver.session_id
                _driver = WebDriver.Remote(Config.APPIUM_SERVER_URL, Config.self.desired_caps)
            session_id = _driver.session_id
            print('driver', _driver)
            print('session id', session_id)
        return _driver

    def get_driver_no_app(self):
        global _driver
        if _driver is None:
            try:
            #    _driver = WebDriver(Config.APPIUM_SERVER_URL, self.desired_caps)
                _driver = webdriver.Remote(Config.APPIUM_SERVER_URL, self.desired_caps_no_app)

            except Exception as e:
                print(e)
                Config.self.desired_caps['sessionId'] = _driver.session_id
                _driver = WebDriver.Remote(Config.APPIUM_SERVER_URL, Config.self.desired_caps)
            session_id = _driver.session_id
            print('driver', _driver)
            print('session id', session_id)
        return _driver


    def teardown_driver():
        global _driver
        if _driver is not None:
            _driver.quit()
            _driver = None
            