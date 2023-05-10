from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class AlertHelper:
    def __init__(self, driver):
        self.driver = driver
        
    def switch_to_alert(self):
        try:
            WebDriverWait(self.driver, 50).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except TimeoutException:
            print("No alert is present on the screen")
            return None
    
    def show_alert(self, message):
        
        alert = self.driver.switch_to.alert
        alert.send_keys(message)
        alert.accept()