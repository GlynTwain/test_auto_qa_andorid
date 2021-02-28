from py_code.features.application import Application
from appium import webdriver

"""behave -f allure_behave.formatter:AllureFormatter -o reports/ features"""
def before_scenario(context,scenario):


    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "9",
        "app": "/home/glyntwain/Документы/Prog/test_auto_qa_andorid/com.xaxtix.team.waterillunimation_1_apps.evozi.com.apk",
    }
#D:\Работа\pytz\com.xaxtix.team.waterillunimation_1_apps.evozi.com.apk
    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)

def after_scenario(context,scenario):
    context.driver.quit()