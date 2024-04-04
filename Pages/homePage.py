from selenium.webdriver.common.by import By

from Pages.base import Base


class homePage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def do_click_on_leave(self):
        leave_option = self.getElement(By.XPATH, "//span[text()='Leave']")
        self.clickElement(leave_option)

