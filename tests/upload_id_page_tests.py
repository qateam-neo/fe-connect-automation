
from pages.upload_id.upload_id import UploadIdPage

# Define the test case
def test_upload_id_page(driver):
    upload_id_page = UploadIdPage(driver)
    upload_id_page.upload_front_back_ids()