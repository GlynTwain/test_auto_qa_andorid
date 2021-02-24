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

    def wait(self, *locator):
        self.driver.find_element(*locator).implicitly_wait(10)
