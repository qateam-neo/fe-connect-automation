import time

from pages.base_page import BasePage
from pages.investment_proposal.customized_plan.customized_plan_config import \
    AGE
from pages.investment_proposal.customized_plan.customized_plan_locators import \
    CustomizedPlanLocators


class CustomizedPlanPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # @handle_exceptions
    def fill_customized_plan(self):
        self.choose_primary_reason()
        self.choose_age()
        self.choose_monthly_income()
        time.sleep(1)
        self.choose_household()
        self.choose_total_value()
        time.sleep(1)
        self.answer_lower_investment_returns_question()
        self.answer_bigger_investment_risks_question()

    def choose_primary_reason(self):
        primary_reason_locator = CustomizedPlanLocators.PRIMARY_REASON_COMBO
        self.wait_and_click_element_by_xpath(primary_reason_locator)
        primary_reason_item_locator = CustomizedPlanLocators.PRIMARY_REASON_ITEM_XPATH
        self.wait_and_click_element_by_xpath(primary_reason_item_locator)


        
    def choose_age(self):
        age_field_locator = CustomizedPlanLocators.AGE_FIELD
        self.wait_and_fill_input_field_by_xpath(age_field_locator, AGE)


    def choose_monthly_income(self):
        monthly_income_combo_locator = CustomizedPlanLocators.MONTHLY_INCOME_COMBO
        self.wait_scroll_vertically_to_element_by_xpath_and_fill(monthly_income_combo_locator)

        monthly_income_item_locator = CustomizedPlanLocators.MONTHLY_INCOME_ITEM_ID
        self.wait_and_click_element_by_xpath(monthly_income_item_locator)


    def choose_household(self):
        household_combo_locator = CustomizedPlanLocators.HOUSEHOLD_COMBO
        self.wait_and_click_element_by_xpath(household_combo_locator)

        household_item_locator = CustomizedPlanLocators.HOUSEHOLD_ITEM_XPATH
        self.wait_and_click_element_by_xpath(household_item_locator)

            
    def choose_total_value(self):
        total_value_combo_locator = CustomizedPlanLocators.TOTAL_VALUE_COMBO
        self.wait_and_click_element_by_xpath(total_value_combo_locator)
        total_value_item_locator = CustomizedPlanLocators.TOTAL_VALUE_ITEM_XPATH
        self.wait_and_click_element_by_xpath(total_value_item_locator)


    def answer_lower_investment_returns_question(self):
        lower_investment_returns_combo_locator = CustomizedPlanLocators.LOWER_INVESTMENTS_RETURNS_COMBO
        self.wait_and_click_element_by_xpath(lower_investment_returns_combo_locator)
        lower_investment_returns_item_locator =  CustomizedPlanLocators.LOWER_INVESTMENTS_RETURNS_ITEM_XPATH
        self.wait_and_click_element_by_xpath(lower_investment_returns_item_locator)
        

    def answer_bigger_investment_risks_question(self):
        bigger_investment_risks_combo_locator = CustomizedPlanLocators.BIGGER_INVESTMENT_RISKS_COMBO
        self.wait_scroll_vertically_to_element_by_xpath_and_fill(bigger_investment_risks_combo_locator)
        bigger_investment_risks_item_locator = CustomizedPlanLocators.BIGGER_INVESTMENT_RISKS_ITEM
        self.wait_scroll_vertically_to_element_by_xpath_and_fill(bigger_investment_risks_item_locator)
        # wait = WebDriverWait(self.driver, 50)

        # WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((AppiumBy.XPATH, ))).click()

    def answer_worry_about_losing_money_question(self):
        worry_about_losing_money_combo_locator = CustomizedPlanLocators.WORRY_ABOUT_LOSING_MONEY_COMBO
        self.wait_and_click_element_by_xpath(worry_about_losing_money_combo_locator)
        worry_about_losing_money_item_locator = CustomizedPlanLocators.WORRY_ABOUT_LOSING_MONEY_ITEM
        self.wait_and_click_element_by_xpath(worry_about_losing_money_item_locator)
        

 # def choose_monthly_income(self):
        # wait = WebDriverWait(self.driver, 50)
        # monthly_income_combo = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, CustomizedPlanLocators.MONTHLY_INCOME_COMBO)))
        # # Scroll down the page using TouchAction
        # # action = TouchAction(self.driver)
        # # action.press(x=500, y=1500).wait(500).move_to(x=500, y=1200).wait(500).release().perform()

        # # actions = TouchAction(self.driver)
        # # actions.press(monthly_income_combo).move_to(x=0, y=600).release().perform()

        # self.swipe_helper.scroll_vertically_to_element(monthly_income_combo)
        # # self.swipe_helper.scroll_down_to_middle()
        # wait.until(EC.visibility_of(monthly_income_combo))
        # try:
        #     monthly_income_combo.click()
        #     WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.XPATH, CustomizedPlanLocators.MONTHLY_INCOME_ITEM_ID))).click()
    
        # except Exception as e:
        #     print(f"Failed to click monthly income combo element: {e}")



        #screenshotContainer > div.ant-spin-nested-loading > div > div > div > div > div._highlighter-box_b7f25._inspected-element-box_b7f25