import random
import time

from pages.base_page import BasePage
from pages.investment_proposal.predefined_plan.config import ELEMENTS


class PredefinedFlow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.choice= random.choice([ELEMENTS.CONSERVATIVE_OPTION,ELEMENTS.BALANCED_OPTION,ELEMENTS.GROWTH_OPTION])

    def start(self):
        # self.click_element(self.choice)
        self.click_hidden_element(ELEMENTS.CONSERVATIVE_OPTION)
        self.click_hidden_element(ELEMENTS.CONTINUE_BUTTON)


    # def click_customized_plan(self):
    #     self.swipe_helper.swipe_from_top_to_bottom()
    #     customized_plan_text_button = PredefinedPlanLocators.CUSTOMIZED_PLAN_TEXT_BUTTON
    #     self.wait_and_click_element_by_xpath(customized_plan_text_button)

    # def start(self):
        