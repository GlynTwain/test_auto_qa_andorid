from screens.base import Screen
from selenium.webdriver.common.by import By


class MainScreen(Screen):
    BUTTON_NEXT = (By.ID, "com.xaxtix.team.waterillunimation:id/button")
    BUTTON_GO = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView")
    ANIM_FLASH = (By.ID, "b7754909-d18a-4446-b38b-cb971a901c85")
    BUTTON_CLOSE = (By.ID,"34c34ad5-d317-42e7-83a9-d82361787983")

    def tap_next(self):
        self.click(*self.BUTTON_NEXT)

    def tap_go(self):
        self.click(*self.BUTTON_GO)

    def get(self):
        result = self.get_info(*self.ANIM_FLASH, attr='text')
        assert result == "Вода освещена Наслаждайтесь", f'{result} вместо Вода освещена Наслаждайтесь'

    def tap_close(self):
        self.click(*self.BUTTON_CLOSE)


