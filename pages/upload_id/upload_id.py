import os
import time

from pages.base_page import BasePage
from pages.upload_id.upload_id_config import UploadIdConfig
from pages.upload_id.upload_id_locators import UploadIdPageLocators


class UploadIdPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.upload_id_by_camera = UploadIdConfig.UPLOAD_ID_BY_CAMERA
    
    def upload_front_back_ids(self):
        self.upload_front_id()
        self.upload_back_id()


    def upload_front_id(self):
        self.click_upload_front_button()
        self.click_allow_button_permission()
        self.click_upload_front_button()
        self.click_allow_button_permission()
        self.click_upload_front_button()
        if self.upload_id_by_camera:
            self.take_photo()
        else:
            self.click_files_button()

    def upload_back_id(self):
        self.click_upload_back_button()
        if self.upload_id_by_camera:
            self.take_photo()
        else:
            self.click_files_button()
        self.click_submit_button()

    def click_upload_front_button(self):
        upload_front_button_locator = UploadIdPageLocators.UPLOAD_FRONT_BUTTON
        self.wait_and_click_element_by_xpath(upload_front_button_locator)


    def click_upload_back_button(self):
        upload_back_button_locator = UploadIdPageLocators.UPLOAD_BACK_BUTTON
        self.wait_and_click_element_by_xpath(upload_back_button_locator)

    def click_allow_button_permission(self):
        time.sleep(5)
        allow_button_locator = UploadIdPageLocators.ALLOW_BUTTON
        self.wait_and_click_element_by_id(allow_button_locator)


    def take_photo(self):
        camera_element_locator = UploadIdPageLocators.CAMERA_OPTION
        self.wait_and_click_element_by_xpath(camera_element_locator)
       
        take_photo_locator = UploadIdPageLocators.TAKE_PHOTO
        self.wait_and_click_element_by_xpath(take_photo_locator)
 
        okay_button_locator = UploadIdPageLocators.OKAY_BUTTON
        self.wait_and_click_element_by_id(okay_button_locator)


    def click_submit_button(self):
        submit_button_locator = UploadIdPageLocators.SUBMIT_BUTTON
        self.wait_and_click_element_by_xpath(submit_button_locator)


    def click_files_button(self):
        files_option_locator = UploadIdPageLocators.FILES_OPTION
        file_path = os.path.abspath(UploadIdPageLocators.FILE_PATH)
        self.wait_and_click_element_by_xpath(files_option_locator)
        self.wait_and_upload_file(file_path)


        