from selenium.webdriver.common.by import By

class ELEMENTS:
    # CONSERVATIVE_OPTION ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView[2]'
    BALANCED_OPTION = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView[5]'
    GROWTH_OPTION = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView[6]'
    # CONTINUE_BUTTON = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View/android.widget.Button'
    CUSTOMIZED_PLAN_TEXT_BUTTON = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView[8]'
    
    
    CONSERVATIVE_OPTION={
        "locator":By.XPATH,
        "value":"//android.widget.TextView[contains(@text, 'Conservative')]",
        "text":None
    }
    
    CONTINUE_BUTTON={
        "locator":By.XPATH,
        "value":"//android.widget.Button[contains(@text, 'Continue')]",
        "text":None
    }