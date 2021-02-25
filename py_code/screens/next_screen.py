from py_code.screens.base import Screen
from selenium.webdriver.common.by import By


class Next_screen(Screen):
    BUTTON = (By.ID, "com.xaxtix.team.waterillunimation:id/button")

    def swipe_side(self, direction: str):
        direction.lower()

        if direction == "влево":
            self.swipe(self, x1=977, y1=803, x2=136, y2=800)
        elif direction == "вправо":
            self.swipe(self, x1=136, y1=800, x2=977, y2=803)
        else:
            assert 'Нет заданного направления'

