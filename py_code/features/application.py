from py_code.screens import MainScreen
from py_code.screens import Next_screen

class Application:

    def __init__(self,driver):
        self.main_screen = MainScreen(driver)
        self.next_screen = Next_screen(driver)
