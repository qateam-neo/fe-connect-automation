import time

from pages.base_page import BasePage
from pages.investment_proposal.predefined_plan.predefined_plan_locators import \
    PredefinedPlanLocators


class PredefinedPlanPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_predefined_investment_plan(self):
        time.sleep(2)
        self.click_investment_plan()
        self.click_continue_button()

    def click_investment_plan(self):
        time.sleep(5)
        conservative_option = PredefinedPlanLocators.CONSERVATIVE_OPTION
        self.wait_and_click_element_by_xpath(conservative_option)

    def click_continue_button(self):
        continue_button = PredefinedPlanLocators.CONTINUE_BUTTON
        self.wait_and_click_element_by_xpath(continue_button)

    def click_customized_plan(self):
        self.swipe_helper.swipe_from_top_to_bottom()
        customized_plan_text_button = PredefinedPlanLocators.CUSTOMIZED_PLAN_TEXT_BUTTON
        self.wait_and_click_element_by_xpath(customized_plan_text_button)
