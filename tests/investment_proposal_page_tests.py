
from pages.investment_proposal.predefined_plan.predefined_plan import PredefinedPlanPage
from pages.investment_proposal.customized_plan.customized_plan import CustomizedPlanPage
from pages.investment_proposal.investment_proposal import InvestmentProposalPage
from pages.investment_proposal.investment_proposal_config import PREDEFINED_PLAN

import time


# Define the test case
def test_investment_proposal_page(driver):
    predefined_plan = PREDEFINED_PLAN
    predefined_plan_page = PredefinedPlanPage(driver)

    if predefined_plan:   
        time.sleep(1)
        predefined_plan_page.click_investment_plan()
        predefined_plan_page.click_continue_button()
        time.sleep(1)
    else:
        predefined_plan_page.click_customized_plan()
        
        customized_plan_page = CustomizedPlanPage(driver)
        customized_plan_page.fill_customized_plan()

    investment_proposal_page = InvestmentProposalPage(driver)
    investment_proposal_page.click_continue_button()