from appium.webdriver.common.appiumby import AppiumBy

class ELEMENTS:
    
    
    CONTINUE_BUTTON_XPATH = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.Button'
    # CHANGE_MY_NAME_BUTTON_XPATH = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.TextView[2]'
    CHANGE_MY_NAME_BUTTON={
        "locator":AppiumBy.CLASS_NAME,
        "value":"android.widget.TextView",
        "text":"Change my name"
    }

    FIRST_NAME_FIELD ={
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="first_name"]',
        "text": None
    }

    MIDDLE_NAME_FIELD ={
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="middle_name"]',
        "text": None
    }

    LAST_NAME_FIELD ={
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="family_name"]',
        "text": None
    }

    CHANGE_MY_NAME_CONTINUE_BUTTON ={
        "locator":AppiumBy.CLASS_NAME,
        "value":"android.widget.Button",
        "text": "Continue"
    }


    CONTINUE_BUTTON_TO_FILL_NAME_PAGE = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.Button'
    FIRST_NAME_COMBO = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View/android.view.View[1]'
    FIRST_NAME_ITEM = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View/android.view.View[1]/android.view.View/android.widget.TextView[1]'
    LAST_NAME_COMBO = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View/android.view.View[3]'
    LAST_NAME_ITEM = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View/android.view.View[3]/android.view.View/android.widget.TextView[2]'
    
    CHOOSE_NAME_PAGE_CONTINUE_BUTTON = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.widget.Button'
    CHOOSE_MIDDLE_NAME_PAGE_CONTINUE_BUTTON = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.widget.Button'
    NATIONALITY_COMBO_OLD = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.TextView'
    NATIONALITY_COMBO = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]'
    NATIONALITY_ITEM = '//*[@resource-id="react-select-2-option-1"]'

 
    # PASSPORT_NUMBER_FIELD = '//*[@resource-id="passport_number"]'
    # PASSPORT_COUNTRY_COMBO = '//*[@resource-id="react-select-10-placeholder"]'
    # PASSPORT_COUNTRY_ITEM = '//*[@resource-id="react-select-10-option-0"]'
    # PASSPORT_EXPIRY_DATE_FIELD = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]/android.view.View/android.widget.EditText'
    # PASSPORT_EXPIRY_DATE_FIELD_OLD = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View/android.view.View[5]/android.view.View/android.widget.EditText'
    # PASSPORT_EXPIRY_DATE_FIELD_OLD_OLD = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.widget.EditText'
    
