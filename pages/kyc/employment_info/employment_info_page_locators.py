from appium.webdriver.common.appiumby import AppiumBy

class EmploymentInfoPageIDs:
    SCREEN_TRIGGER_IDENTIFICATION={
        "locator":AppiumBy.XPATH,
        "value":'//*[contains(@text,"Income information")]',
        "text": None
    }
    
    EMPLOYMENT_SECTION = {
        "locator":AppiumBy.XPATH,
        "value":'//android.widget.TextView[contains(@text,"Employment")]',
        "text":None
    }
    EMPLOYMENT_COMBO =  {
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="react-select-9-placeholder"]' ,
        "text":None
    }
    EMPLOYMENT_ITEM = {
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="react-select-9-option-1"]' ,
        "text":None
    } 

    # EMPLOYMENT_SECTION_COMPLETED = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[1]/android.widget.TextView[1]'
    EMPLOYMENT_SECTION_COMPLETED = {
        "locator":AppiumBy.XPATH,
        "value":'//android.widget.TextView[contains(@text,"Employment")]',
        "text":None
    }
    BOARD_MEMBERSHIP_SWITCH_BUTTON= {
        "locator":AppiumBy.XPATH,
        "value":'//android.widget.TextView[contains(@text,"Board")]',
        "text":None
    }

    INCOME_INFORMATION_SECTION = {
        "locator":AppiumBy.XPATH,
        "value":'//android.widget.TextView[contains(@text,"Income information")]',
        "text":None
    }

    PRIMARY_OBJECTIVE_COMBO =  {
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="react-select-10-placeholder"]',
        "text":None
    }
    PRIMARY_OBJECTIVE_ITEM =  {
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="react-select-10-option-3"]',
        "text":None
    }
    ANNUAL_INCOME_COMBO =  {
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="react-select-11-placeholder"]',
        "text":None
    }
 
    ANNUAL_INCOME_ITEM ={
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="react-select-11-option-1"]' ,
        "text":None
    } 

    SOURCE_OF_INCOME_COMBO ={
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-12-placeholder"]',
        "text":None
    }  

    SOURCE_OF_INCOME_ITEM ={
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-12-option-1"]',
        "text":None
    }  

    DETAILS_OF_INCOME_TOP={
        "locator":AppiumBy.XPATH,
        "value": '//android.view.View[contains(@text,"Source of income")]' ,
        "text":None
    }
    
    # SOURCE_OF_INCOME_ITEM2 = '//*[@resource-id="react-select-12-option-4"]'
    
    # DETAILS_OF_INCOME_TEXT = '//*[@resource-id="income_details"]' 
    # DETAILS_OF_INCOME_TEXT = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[2]/android.view.View[4]/android.view.View/android.widget.EditText'
    # DETAILS_OF_INCOME_TEXT = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View/android.widget.EditText'
    # DETAILS_OF_INCOME_TEXT = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.EditText'
    # DETAILS_OF_INCOME_TEXT = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.EditText'
    DETAILS_OF_INCOME_TEXT = 'income_details'
    
    # SCROLL TO BOTTOM
    TOTAL_VALUE_COMBO ={
        "locator":AppiumBy.XPATH,
        "value":  '//*[@resource-id="react-select-13-placeholder"]',
        "text":None
    }  
    TOTAL_VALUE_ITEM ={
        "locator":AppiumBy.XPATH,
        "value": '//*[@resource-id="react-select-13-option-4"]',
        "text":None
    }  
    VALUE_OF_TRANSACTIONS_COMBO = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.TextView[2]'
    VALUE_OF_TRANSACTIONS_ITEM = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.widget.TextView[3]'
    VALUE_OF_ASSETS_COMBO = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.TextView[2]'
    VALUE_OF_ASSETS_ITEM = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.widget.TextView[1]'
    YEARS_WORKED_IN_FINANCIAL_SECTOR_COMBO = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.widget.TextView[2]'
    YEARS_WORKED_IN_FINANCIAL_SECTOR_ITEM = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View/android.widget.TextView[1]'
    CONTINUE_BUTTON_OLD = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.widget.Button'

    