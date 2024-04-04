import time
from selenium.webdriver.common.by import By

from Pages.base import Base


class leavePage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def do_click_on_apply_option(self):
        apply_option = self.getElement(By.XPATH, "//a[text()='Apply']")
        self.clickElement(apply_option)

    def do_apply_leave(self):
        leave_type_dropdown = self.getElement(By.XPATH, "//div[text()='-- Select --']")
        self.clickElement(leave_type_dropdown)

        leave_type_option = self.getElement(By.XPATH, '//div[@role = "listbox"]//span')
        self.clickElement(leave_type_option)

        from_date_picker = self.getElement(By.XPATH, "//label[contains(text(),'From Date')]/../following-sibling::div")
        self.clickElement(from_date_picker)

        from_date = self.getElement(By.XPATH, "//div[@class='oxd-calendar-date' and text()='27']")
        self.clickElement(from_date)

        time.sleep(2)

        to_date_picker = self.getElement(By.XPATH, "//label[contains(text(),'To Date')]/../following-sibling::div")
        self.clickElement(to_date_picker)

        to_date = self.getElement(By.XPATH, "//div[@class='oxd-calendar-date' and text()='29']")
        self.clickElement(to_date)

        partial_days_dropdown = self.getElement(By.XPATH, "//label[contains(text(),'Partial Days')]/../following-sibling::div")
        self.clickElement(partial_days_dropdown)

        partial_days_option = self.getElement(By.XPATH, "//label[text() = 'Partial Days']/../following-sibling::div//span[text() = 'End Day Only']")
        self.clickElement(partial_days_option)

        end_day_dropdown = self.getElement(By.XPATH, "//label[text() = 'End Day']/../following-sibling::div")
        self.clickElement(end_day_dropdown)

        end_day_option = self.getElement(By.XPATH, "//span[contains(normalize-space(),'Half Day - Morning')]")
        self.clickElement(end_day_option)

        comments = self.getElement(By.XPATH, "//label[contains(text(),'Comments')]/../following-sibling::div/textarea")
        self.sendKeys(comments, "Test")

        apply_button = self.getElement(By.XPATH, "//button[contains(normalize-space(),'Apply')]")
        self.clickElement(apply_button)

        my_leave = self.getElement(By.XPATH, "//a[text()='My Leave']")
        self.clickElement(my_leave)




