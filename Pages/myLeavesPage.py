import time
from selenium.webdriver.common.by import By

from Pages.base import Base


class myLeavesPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def view_leave_details(self):
        three_dot_button = self.getElement(By.XPATH, "//div[@class='oxd-table-body']/div//div[text()='Test']/../following-sibling ::div//button[text()=' Cancel ']/following-sibling::li/button")
        self.clickElement(three_dot_button)

        view_details_option = self.getElement(By.XPATH, "//div[@class='oxd-table-body']/div//div[text()='Test']/../following-sibling ::div//button[text()=' Cancel ']/following-sibling::li/ul//p[text()='View Leave Details']")
        self.clickElement(view_details_option)