from config import Config
from pages.base_page import BasePage
from pages.login.login_locators import LoginPageLocators


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
        print('petra')
        self.enter_civil_id()
        self.click_load_token()
        self.click_pop_up_button()
        self.click_connect_web_view_button()

    def enter_civil_id(self):
        civil_id_field_locator = LoginPageLocators.CIVIL_ID_FIELD
        self.wait_and_fill_input_field_by_id(civil_id_field_locator, Config.CIVIL_ID_NUMBER)


    def click_load_token(self):
        load_token_button_locator = LoginPageLocators.LOAD_TOKEN_BUTTON
        self.wait_and_click_element_by_id(load_token_button_locator)

    def click_delete_civil_id(self):
        delete_button_locator = LoginPageLocators.DELETE_BUTTON
        self.wait_and_click_element_by_id(delete_button_locator)

    def click_pop_up_button(self):
        popup_ok_button_locator = LoginPageLocators.POPUP_OK_BUTTON
        self.wait_and_click_element_by_id(popup_ok_button_locator)

    def click_connect_web_view_button(self):
        pj_connect_webview_button_locator = LoginPageLocators.PJ_CONNECT_WEBVIEW
        self.wait_and_click_element_by_id(pj_connect_webview_button_locator)

