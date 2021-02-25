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

    def get_info(self, *locator, attr: str)->str:
        pole = self.find_element(*locator).get_attribute(attr)
        return str(pole)

    def wait(self, time: int = 15):
        self.driver.implicitly_wait(time)

    def swipe(self, x1: int, y1: int, x2: int, y2: int):
        touch = TouchAction(self.driver)
        touch.press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()
        time.sleep(1)
