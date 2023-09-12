from config import UserData
from pages.base_page import BasePage
from pages.investment_proposal.customized_plan.main import CustomizedFlow
from pages.investment_proposal.predefined_plan.main import PredefinedFlow


class OnboardingFlow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def start(self):
        if UserData.is_predefined:
            PredefinedFlow(self.driver).start()
        else:
            CustomizedFlow(self.driver).start()
            
        