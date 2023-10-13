from appium.webdriver.common.appiumby import AppiumBy

class WealthInfoPageLocators:
    WEALTH_INFORMATION_SECTION  = {
        "locator":AppiumBy.XPATH,
        "value":'//*[@resource-id="std-section"]',
        "index":1,
        "text": None
    }
    PURPOSE_COMBO = '//*[@resource-id="react-select-14-placeholder"]'
    PURPOSE_ITEM = '//*[@resource-id="react-select-14-option-3"]'
    LEVEL_OF_INVESTMENT_KNOWLEDGE_COMBO = '//*[@resource-id="react-select-15-placeholder"]'
    LEVEL_OF_INVESTMENT_KNOWLEDGE_ITEM = '//*[@resource-id="react-select-15-option-0"]'
    INVESTMENT_EXPERIENCE_COMBO = '//*[@resource-id="react-select-16-placeholder"]'
    INVESTMENT_EXPERIENCE_ITEM = '//*[@resource-id="react-select-16-option-1"]'
    RISK_TOLERANCE_COMBO = '//*[@resource-id="react-select-17-placeholder"]'
    RISK_TOLERANCE_ITEM = '//*[@resource-id="react-select-17-option-1"]'
    # scroll to bottom
    WEALTH_AMOUNT_TEXT = '//*[@resource-id="wealth_amount"]'
    SOURCE_OF_WEALTH_COMBO = '//*[@resource-id="react-select-18-placeholder"]'
    SOURCE_OF_WEALTH_ITEM = '//*[@resource-id="react-select-18-option-0"]'
    WEALTH_DETAILS_TEXT = '//*[@resource-id="wealth_details"]'
    CONTINUE_BUTTON = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.Button'