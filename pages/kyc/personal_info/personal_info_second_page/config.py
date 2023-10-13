from appium.webdriver.common.appiumby import AppiumBy
class ELEMENTS:
    

    # PERSONAL_INFORMATION_SECTION ={

    #     "locator":AppiumBy.XPATH,
    #     "value":'//*[@resource-id="std-section"]',
    #     "text": None
    # }    
    
# '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[1]'
    PERSONAL_INFORMATION_SECTION = {
        "locator":AppiumBy.CLASS_NAME,
        "value":'android.widget.TextView',
        "text":"Personal Information",
    }
    CONTACT_INFORMATION_SECTION = {
        "locator":AppiumBy.CLASS_NAME,
        "value":'android.widget.TextView',
        "text":"Contact and Address",

    }

    CIVIL_ID_SERIAL_FIELD ={

        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="civil_id_serial"]',
        "text": None
    }    
    
    CIVIL_ID_EXPIRY_DATE_FIELD ={
        "locator":AppiumBy.XPATH,
        "value": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText',
        "text":None
    }
    
    PASSPORT_NUMBER_FIELD = {

        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="passport_number"]',
        "text": None
    } 
       
    PASSPORT_COUNTRY_COMBO = {

        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-10-placeholder"]',
        "text": None
    } 
    PASSPORT_COUNTRY_ITEM = {

        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-10-option-0"]',
        "text": None
    } 
    PASSPORT_EXPIRY_DATE_FIELD = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]/android.view.View/android.widget.EditText'
    PASSPORT_EXPIRY_DATE_FIELD_OLD = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View/android.view.View[5]/android.view.View/android.widget.EditText'
    PASSPORT_EXPIRY_DATE_FIELD_OLD_OLD = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.widget.EditText'
    

    MOTHER_FULL_NAME_FIELD = {

        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="mother_name"]',
        "text": None
    } 
    
    CHILDREN_NUMBER_COMBO = {
        
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-6-placeholder"]',
        "text": "How many children do you have?"
    }
    
    CHILDREN_NUMBER_COMBO2 ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.Image'

    CHILDREN_NUMBER_ITEM ={
        
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-6-option-0"]',
        "text": None
    } 

    CHILDREN_NAME_FIELD_1 = '//*[@resource-id="children_name_1"]'
    CHILDREN_CLASS_NAME = '_highlighter-box_b7f25 _inspected-element-box_b7f25'

    CONTACT_ADDRESS_SECTION = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]'
    CONTACT_ADDRESS_SECTION2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView[1]'
    EMAIL_TEXT_BOX_FIELD = {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="email"]',
        "text": None
    } 
    
    CONFIRM_EMAIL_TEXT_BOX_FIELD = {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="email-confirm"]',
        "text": None
    } 

    CONTACT_MOBILE_NUMBER_FIELD =  {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="contact_mobile_number"]' ,
        "text": None
    } 
    
    CITY_COMBO ={
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-7-placeholder"]',
        "text": None
    } 
    
    CITY_ITEM = {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-7-option-3"]',
        "text": None
    }

    AREA_COMBO = {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-8-placeholder"]',
        "text": None
    }
    
    AREA_COMBO_ITEM = {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-8-option-0"]',
        "text": None
    }
    




    ADDRESS_BLOCK_FIELD = {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="address_block"]',
        "text": None
    }
    STREET_FIELD = {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="address_street"]',
        "text": None
    }
    AVENUE_FIELD = {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="address_avenue"]',
        "text": None
    }
    HOUSE_FIELD = {
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="address_house"]',
        "text": None
    }

    CONTINUE_BUTTON_SECOND_INFO_PAGE1 ={
        "locator":AppiumBy.CLASS_NAME,
        "value":"android.widget.Button",
        "text":None
    } 