from selenium import webdriver
from Pages import base
from Pages import leavePage
from Pages import myLeavesPage
from Pages import leaveDetailsPage
from Pages import loginPage
from Pages import homePage

def main():
    driver = webdriver.Chrome()

    login_page = loginPage.loginPage(driver)
    login_page.get_url()
    login_page.do_login("Admin","admin123")

    home_page = homePage.homePage(driver)
    home_page.do_click_on_leave()

    leave_page = leavePage.leavePage(driver)
    leave_page.do_click_on_apply_option()
    leave_page.do_apply_leave()

    my_leave_page = myLeavesPage.myLeavesPage(driver)
    my_leave_page.view_leave_details()

    leave_details_page = leaveDetailsPage.leaveDetailsPage(driver)
    leave_details_page.cancel_leave()

    logout = base.Base(driver)
    logout.logout()

if __name__ == "__main__":
    main()
