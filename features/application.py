from screens.main_screen import MainScreen
from screens.next_screen import Next_screen

class Application:

    def __init__(self,driver):
        self.main_screen = MainScreen(driver)
        self.next_screen = Next_screen(driver)
