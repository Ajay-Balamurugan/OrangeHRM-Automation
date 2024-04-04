from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self,driver):
        self.driver = driver

    def getElement(self, locator, value):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((locator, value)))
    def sendKeys(self, element, value):
        element.send_keys(value)

    def clickElement(self, element):
        element.click()

    def logout(self):
        user_dropdown = self.getElement(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.clickElement(user_dropdown)

        logout_option = self.getElement(By.XPATH, "//span[@class='oxd-userdropdown-tab']/following-sibling::ul/li/a[text()='Logout']")
        self.clickElement(logout_option)

    def get_url(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()