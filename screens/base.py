import time

from appium.webdriver.common.touch_action import TouchAction


class Screen:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        e = self.find_element(*locator)
        e.click()

    def get_info(self, *locator, attr: str):
        pole = self.find_element(*locator).get_attribute(attr)
        return pole

    def wait(self):
        self.driver.implicitly_wait(15)

    def swipe(self):
        touch = TouchAction(self.driver)
        touch.press(x=977, y=803).move_to(x=136, y=800).release().perform()
        time.sleep(1)

