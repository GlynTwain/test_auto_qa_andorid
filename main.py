from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "app": "D:\Работа\pytz\com.xaxtix.team.waterillunimation_1_apps.evozi.com.apk",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
