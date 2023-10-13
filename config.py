class Config:
    PLATFORM_NAME = "Android"
    PLATFORM_VERSION = "13.0"
    DEVICE_NAME = "Android Emulator"
    UDID = "emulator-5554"
    APP = "/Users/mohamadharb/Downloads/PJ-Connect.apk"
    

    SESSION_ID = 'b965060e-73bc-437e-b9ba-12670bc02203'
    APPIUM_SERVER_URL = 'http://127.0.0.1:4722/wd/hub'
    # CIVIL_ID_NUMBER = '896545666'
    CIVIL_ID_NUMBER = '114718725' #Exception mode off

    # CIVIL_ID_NUMBER = '000939692' #Exception mode on
    DELETE_CIVIL_ID = True
    CLOSE_APP_BUTTON = 'com.example.myapplication.dynamic:id/closeButton'
    CONFIRM_CLOSE_BUTTON = 'android:id/button1'
    
    # capabilities that specify the characteristics of the mobile device and the app to be tested.
    desired_caps = {
        "platformName": PLATFORM_NAME,
        "platformVersion": PLATFORM_VERSION,
        "deviceName": DEVICE_NAME,
        "udid": UDID,
        "app": APP
    }
    
class UserData: 
    is_predefined=True    
