import time
# *  This import allows us to use Appium's By class to locate elements within a native mobile app or a web view.
from appium.webdriver.common.appiumby import AppiumBy
# * This import provides the ActionChains class, which allows us to perform complex actions like click-and-hold, drag-and-drop, or double-click.
from selenium.webdriver.common.action_chains import ActionChains
# *  This import provides Selenium's By class to locate elements within a web page or web view.
from selenium.webdriver.common.by import By
# * This import provides the WebDriverWait class, which allows us to wait for certain conditions to be met before continuing with test execution.
from selenium.webdriver.support.ui import WebDriverWait
# * This import provides a set of common conditions that can be used with Selenium's WebDriverWait class to wait for certain conditions to be met before continuing with test execution.
from selenium.webdriver.support import expected_conditions as EC

from helpers.swipe_helper import SwipeHelper
from utils.handler.exception_handler import handle_exceptions


class LocatorHelper:  

    def __init__(self, driver):
        self.driver = driver
        self.swipe_helper = SwipeHelper(self.driver)

    @handle_exceptions
    def wait_and_click_element(self, locator):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
        element.click()

    @handle_exceptions
    def wait_and_upload_file(self, file_path):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//input[@type='file']")))
        element.send_keys(file_path)
        

    @handle_exceptions
    def wait_and_click_element_by_id(self, locator):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((By.ID, locator)))
        element.click()

    @handle_exceptions
    def wait_and_fill_input_field(self, locator, value):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))
        element.clear()
        element.send_keys(value)

    @handle_exceptions
    def wait_and_set_element_value(self,locator, value):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))

        # Tap on the element to give it focus and bring up the keyboard
        element.click()
        action = ActionChains(self.driver)
        action.send_keys(value).perform()
        # Send key events to the device to simulate typing
        # for character in value:
        #     self.driver.keyevent(ord(character))


    @handle_exceptions
    def wait_and_fill_input_field_by_id(self, locator, value):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((By.ID, locator)))
        element.clear()
        element.send_keys(value)

    @handle_exceptions  
    def find_element(self, locator, value):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        element.clear()
        element.send_keys(value)

    @handle_exceptions
    def wait_and_scroll_vertically_to_element(self, locator):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))
        self.swipe_helper.scroll_vertically_to_element(element)
        element.click()

    @handle_exceptions
    def wait_scroll_vertically_to_element_and_fill(self, locator, value):
        # self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
        self.swipe_helper.scroll_vertically_to_element(element)
        
        # self.driver.execute_script("arguments[0].value = arguments[1]", element, value)
        # element = Element(element.id, element.parent)
        # element.set_value(value)
        action = ActionChains(self.driver)
        element.clear()
        action.move_to_element(element).click().perform()
        time.sleep(1) # Add a delay here to give the element time to receive the click event
        action.send_keys(value).perform()
        #     action = ActionChains(self.driver)
        # action.move_to_element(element).click().perform()
        # time.sleep(1) # Add a delay here to give the element time to receive the click event
        
        # for char in value:
        #     action.send_keys(char).perform()

    def wait_and_find_element_by_css_selector(self, locator):
        
        wait = WebDriverWait(self.driver, 50)
        # element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
        # element = self.driver.find_element_by_css_selector('._highlighter-box_b7f25._inspected-element-box_b7f25')
        # element = self.driver.find_element(By.CSS_SELECTOR, locator)
       
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        # self.driver.click_element(element)
        element.click()
