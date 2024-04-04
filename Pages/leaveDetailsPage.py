import time
from selenium.webdriver.common.by import By

from Pages.base import Base


class leaveDetailsPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def cancel_leave(self):
        cancel_button = self.getElement(By.XPATH, "//button[text()=' Cancel ']")
        self.clickElement(cancel_button)