import random
import time

from pages.base_page import BasePage
from pages.investment_proposal.historical_performance.config import ELEMENTS


class HistoricalPerformanceFlow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def start(self):
        self.swipe_helper.swipe_from_top_to_bottom()
        self.click_element(ELEMENTS.CONTINUE_BUTTON)


    # def click_customized_plan(self):
    #     self.swipe_helper.swipe_from_top_to_bottom()
    #     customized_plan_text_button = PredefinedPlanLocators.CUSTOMIZED_PLAN_TEXT_BUTTON
    #     self.wait_and_click_element_by_xpath(customized_plan_text_button)

    # def start(self):
        