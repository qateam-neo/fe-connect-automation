from time import sleep
from pages.base_page import BasePage
from pages.get_started.config import ELEMENTS


class GetStartedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def start(self):
        while not self.is_element_visible(ELEMENTS.GET_STARTED_BUTTON,10,4) and self.wait_and_get_element_by_text("mode") == False:
            pass
        
        if self.is_element_visible(ELEMENTS.GET_STARTED_BUTTON,10,4):
            self.swipe_helper.swipe_from_top_to_bottom()
            sleep(2)
            self.click_hidden_element(ELEMENTS.GET_STARTED_BUTTON)
        else:
            self.wait_and_get_element_by_text("mode")
            print("MODE NEEDED")

    
        

