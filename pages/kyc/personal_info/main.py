from pages.base_page import BasePage
from pages.kyc.personal_info.personal_info_first_page.main import PersonalInfoFirstScreen
from pages.kyc.personal_info.personal_info_second_page.main import PersonalInfoSecondScreen


class PersonalInfoFullFlow(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        
        
    def start(self): 
        PersonalInfoFirstScreen(self.driver).start()
        PersonalInfoSecondScreen(self.driver).start()
        