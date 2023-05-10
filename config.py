class Config:
    PLATFORM_NAME = "Android"
    PLATFORM_VERSION = "10.0"
    DEVICE_NAME = "Android Emulator"
    UDID = "2a9d4e64af3f7ece"
    APP = "/home/petra/Downloads/PJ-Connect.apk"

    SESSION_ID = 'b965060e-73bc-437e-b9ba-12670bc02203'
    APPIUM_SERVER_URL = 'http://localhost:4723/wd/hub'
    # CIVIL_ID_NUMBER = '896545666'
    CIVIL_ID_NUMBER = '000939692'
    DELETE_CIVIL_ID = True
    CLOSE_APP_BUTTON = 'com.example.myapplication:id/closeButton'
    CONFIRM_CLOSE_BUTTON = 'android:id/button1'
    
    # capabilities that specify the characteristics of the mobile device and the app to be tested.
    desired_caps = {
        "platformName": PLATFORM_NAME,
        "platformVersion": PLATFORM_VERSION,
        "deviceName": DEVICE_NAME,
        "udid": UDID,
        "app": APP
    }