from config import Config
from pages.base_page import BasePage
from pages.login.config import ELEMENTS
from pages.get_started.config import ELEMENTS as GETSTARTED_ELEMENTS
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.delete_civil_id = Config.DELETE_CIVIL_ID
        print('civil id', self.delete_civil_id)

    def login(self):
        if self.delete_civil_id:
            self.login_delete_civil_id()
        else:
            self.login_to_webview()
            
        if self.is_element_visible(ELEMENTS.MODE_IS_NEEDED,10) is not False:
            self.click_element(ELEMENTS.BACK)
            self.click_element(ELEMENTS.POPUP_OK_BUTTON,3)
            self.click_element(ELEMENTS.PJ_CONNECT_WEBVIEW,5)
            if not self.is_element_visible(GETSTARTED_ELEMENTS.GET_STARTED_BUTTON,8):
                raise ValueError("Error on opening webview, probably showing mode is needed.. ")


    def login_delete_civil_id(self):
        self.enter_civil_id()
        self.click_load_token()
        self.click_pop_up_button()
        self.click_delete_civil_id()
        self.click_pop_up_button()
        self.click_load_token()
        self.click_pop_up_button()
        self.click_connect_web_view_button()

    def login_to_webview(self):
        self.enter_civil_id()
        self.click_load_token()
        self.click_pop_up_button()
        self.click_connect_web_view_button()

    def enter_civil_id(self):
        self.send_keys(ELEMENTS.CIVIL_ID_FIELD,Config.CIVIL_ID_NUMBER)

    def click_load_token(self):
        self.click_element(ELEMENTS.LOAD_TOKEN_BUTTON)

    def click_delete_civil_id(self):
        self.click_element(ELEMENTS.DELETE_BUTTON)

    def click_pop_up_button(self):
        self.click_element(ELEMENTS.POPUP_OK_BUTTON,10)

    def click_connect_web_view_button(self):
        self.click_element(ELEMENTS.PJ_CONNECT_WEBVIEW)

