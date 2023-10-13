import random
import time

from pages.base_page import BasePage
from pages.investment_proposal.historical_performance.config import ELEMENTS


class HistoricalPerformanceFlow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def start(self):
        # if not self.click_element(ELEMENTS.CONTINUE_BUTTON):
        #     self.swipe_helper.swipe_from_top_to_bottom()
        while self.wait_and_get_element_by_text("Investment Plan") or self.wait_and_get_element_by_text("top tier US"):
            self.click_hidden_element(ELEMENTS.CONTINUE_BUTTON)
        print("TEST")


    # def click_customized_plan(self):
    #     self.swipe_helper.swipe_from_top_to_bottom()
    #     customized_plan_text_button = PredefinedPlanLocators.CUSTOMIZED_PLAN_TEXT_BUTTON
    #     self.wait_and_click_element_by_xpath(customized_plan_text_button)

    # def start(self):
        