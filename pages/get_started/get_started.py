from pages.base_page import BasePage
from pages.get_started.get_started_locators import GetStartedLocators


class GetStartedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def click_get_started_button(self):
        get_started_button = GetStartedLocators.GET_STARTED_BUTTON_XPATH
        self.wait_and_click_element_by_xpath(get_started_button)

        

