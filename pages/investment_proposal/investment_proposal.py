from pages.base_page import BasePage
from pages.investment_proposal.investment_proposal_locators import \
    InvestmentProposalLocators


class InvestmentProposalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_continue_button(self):
        investment_proposal_continue_button = InvestmentProposalLocators.INVESTMENT_PROPOSAL_CONTINUE_BUTTON
        self.wait_and_click_element_by_xpath(investment_proposal_continue_button)