from selenium import webdriver
from Pages.base import Base
import time


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()


helper = Base(driver)

# uname_field = helper.getElement("NAME",'username')
# helper.sendKeys(uname_field,"Admin")
#
# pwd_field = helper.getElement("NAME",'password')
# helper.sendKeys(pwd_field,"admin123")
#
# login_btn = helper.getElement("XPATH","//button[contains(normalize-space(),'Login')]")
# helper.clickElement(login_btn)
#
# leave_option = helper.getElement("XPATH","//span[text()='Leave']")
# helper.clickElement(leave_option)

# apply_btn = helper.getElement("XPATH","//a[text()='Apply']")
# helper.clickElement(apply_btn)

# leave_type_dropdown = helper.getElement("XPATH","//div[text()='-- Select --']")
# helper.clickElement(leave_type_dropdown)
#
# dropdown_option = helper.getElement("XPATH",'//div[@role = "listbox"]//span')
# helper.clickElement(dropdown_option)
#
#
# from_date_picker = helper.getElement("XPATH","//label[contains(text(),'From Date')]/../following-sibling::div")
# helper.clickElement(from_date_picker)
#
# from_date = helper.getElement("XPATH","//div[@class='oxd-calendar-date' and text()='27']")
# helper.clickElement(from_date)
#
# time.sleep(2)
#
# to_date_picker = helper.getElement("XPATH","//label[contains(text(),'To Date')]/../following-sibling::div")
# helper.clickElement(to_date_picker)
#
# to_date = helper.getElement("XPATH","//div[@class='oxd-calendar-date' and text()='29']")
# helper.clickElement(to_date)
#
# comment = helper.getElement("XPATH","//label[contains(text(),'Comments')]/../following-sibling::div/textarea")
# helper.sendKeys(comment,"Test")
#
# partial_days_dropdown = helper.getElement("XPATH","//label[contains(text(),'Partial Days')]/../following-sibling::div")
# helper.clickElement(partial_days_dropdown)
#
# end_day_option = helper.getElement("XPATH","//label[text() = 'Partial Days']/../following-sibling::div//span[text() = 'End Day Only']")
# helper.clickElement(end_day_option)
#
# duration_dropdown = helper.getElement("XPATH","//label[text() = 'End Day']/../following-sibling::div")
# helper.clickElement(duration_dropdown)
#
# half_day_morning_option = helper.getElement("XPATH","//span[contains(normalize-space(),'Half Day - Morning')]")
# helper.clickElement(half_day_morning_option)
#
# apply_btn = helper.getElement("XPATH","//button[contains(normalize-space(),'Apply')]")
# helper.clickElement(apply_btn)
#
# time.sleep(2)
#
# my_leave_btn = helper.getElement("XPATH","//a[text()='My Leave']")
# helper.clickElement(my_leave_btn)

# three_dot_btn = helper.getElement("XPATH","//div[@class='oxd-table-body']/div//div[text()='Test']/../following-sibling ::div//button[text()=' Cancel ']/following-sibling::li/button")
# helper.clickElement(three_dot_btn)
#
# time.sleep(2)
#
# view_details_option = helper.getElement("XPATH","//div[@class='oxd-table-body']/div//div[text()='Test']/../following-sibling ::div//button[text()=' Cancel ']/following-sibling::li/ul//p[text()='View Leave Details']")
# helper.clickElement(view_details_option)

# cancel_btn = helper.getElement("XPATH","//button[text()=' Cancel ']")
# helper.clickElement(cancel_btn)

# time.sleep(2)

# user_dropdown = helper.getElement("XPATH","//span[@class='oxd-userdropdown-tab']")
# helper.clickElement(user_dropdown)
#
# logout_option = helper.getElement("XPATH","//span[@class='oxd-userdropdown-tab']/following-sibling::ul/li/a[text()='Logout']")
# helper.clickElement(logout_option)

time.sleep(10)