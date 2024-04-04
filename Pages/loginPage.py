import time

from selenium.webdriver.common.by import By

from Pages.base import Base


class loginPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def do_login(self,username,password):
        username_field = self.getElement(By.NAME, "username")
        password_field = self.getElement(By.NAME, "password")
        login_btn = self.getElement(By.XPATH, "//button[contains(normalize-space(),'Login')]")
        self.sendKeys(username_field,username)
        self.sendKeys(password_field,password)
        self.clickElement(login_btn)

