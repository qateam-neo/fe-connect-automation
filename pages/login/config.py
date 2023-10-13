from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
 
class ELEMENTS:
    CIVIL_ID_FIELD ={ 
        "locator":By.ID,
        "value":"com.example.myapplication.dynamic:id/editTextCivilId",
        "text":None
    }
    LOAD_TOKEN_BUTTON = { 
        "locator":By.ID,
        "value":"com.example.myapplication.dynamic:id/buttonToken",
        "text":None
    }
    DELETE_BUTTON = { 
        "locator":By.ID,
        "value":"com.example.myapplication.dynamic:id/buttonDelete",
        "text":None
    }
    PJ_CONNECT_WEBVIEW = { 
        "locator":By.ID,
        "value":'com.example.myapplication.dynamic:id/buttonWebview',
        "text":None
    }
    POPUP_OK_BUTTON = { 
        "locator":By.ID,
        "value":'android:id/button1',
        "text":None
    }
    
    MODE_IS_NEEDED={
        "locator":AppiumBy.CLASS_NAME,
        "value":"android.widget.TextView",
        "text": 'mode is needed'
    }

    BACK = {
        "locator":AppiumBy.ACCESSIBILITY_ID,
        "value":"Navigate up",
        "text":None
    }