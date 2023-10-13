from config import UserData
from pages.base_page import BasePage
from pages.investment_proposal.config import IDs
from pages.investment_proposal.customized_plan.main import CustomizedFlow
from pages.investment_proposal.predefined_plan.main import PredefinedFlow


class OnboardingFlow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def start(self):
        while not self.is_element_visible(IDs.not_sure_button,timeout=6): print("ERROR: Long time to load")
        
        if UserData.is_predefined:
            PredefinedFlow(self.driver).start()
        else:
            CustomizedFlow(self.driver).start()
            
        