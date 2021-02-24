from screens.base import Screen
from selenium.webdriver.common.by import By

class MainScreen(Screen):
    BUTTON = (By.ID,"com.xaxtix.team.waterillunimation:id/button")

    def tap_next(self):
        self.click(*self.BUTTON)