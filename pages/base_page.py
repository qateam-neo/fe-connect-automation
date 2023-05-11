# base_page.py file can contain common methods or properties shared across pages.
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

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from config import Config
# from helpers.locator_helper import LocatorHelper
from helpers.swipe_helper import SwipeHelper
from utils.handler.exception_handler import handle_exceptions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.swipe_helper = SwipeHelper(self.driver)

    @handle_exceptions
    def wait_and_click_element_by_id(self, element_id):
        element_locator = (By.ID, element_id)
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located(element_locator))
        element.click()


    @handle_exceptions
    def wait_and_click_element_by_xpath(self, locator):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))
        element.click()

    @handle_exceptions
    def wait_and_fill_input_field_by_id(self, locator, value):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((By.ID, locator)))
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
    def wait_and_upload_file(self, file_path):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//input[@type='file']")))
        element.send_keys(file_path)
        
    @handle_exceptions
    def wait_and_fill_input_field_by_xpath(self, locator, value):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))
        element.clear()
        element.send_keys(value)

    @handle_exceptions
    def wait_scroll_vertically_to_element_by_xpath_and_fill(self, locator, value):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
        self.swipe_helper.scroll_vertically_to_element(element)
        action = ActionChains(self.driver)
        element.clear()
        action.move_to_element(element).click().perform()
        time.sleep(1) # Add a delay here to give the element time to receive the click event
        action.send_keys(value).perform()

    @handle_exceptions
    def wait_scroll_vertically_to_element_by_xpath_and_fill_using_digits(self, locator, value):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
        self.swipe_helper.scroll_vertically_to_element(element)
        element.click()
       
        for char in value:
            # use the Android keycode for each character in the value
            # (you can look up the keycodes for each character online)
            keycode = ord(char) - ord('0') + 7
            self.driver.press_keycode(keycode)
            time.sleep(0.2)
        time.sleep(5)
        # hide the keyboard
        self.driver.hide_keyboard()  

    @handle_exceptions
    def wait_and_fill_element_using_digits(self, locator, value):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))
        element.click()
       
        for char in value:
            # use the Android keycode for each character in the value
            # (you can look up the keycodes for each character online)
            keycode = ord(char) - ord('0') + 7
            self.driver.press_keycode(keycode)
            time.sleep(0.2)
        time.sleep(5)
        # hide the keyboard
        self.driver.hide_keyboard()

    @handle_exceptions     
    def close_app(self):
        Config.DELETE_CIVIL_ID = False
        close_app_button_locator = Config.CLOSE_APP_BUTTON
        self.wait_and_click_element_by_id(close_app_button_locator) 
        confirm_close_button_locator = Config.CONFIRM_CLOSE_BUTTON
        self.wait_and_click_element_by_id(confirm_close_button_locator) 