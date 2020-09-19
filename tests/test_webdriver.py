from webdriver_class.webdriver_functions import *


# steps of test case
# launch_website("https://letskodeit.teachable.com/p/practice")
# find_elements_tag('button')
# web_driver_properties()
# web_driver_properties_switch_to_tab()
# close_browser()

# Go back and forward refresh
launch_website("http://automationpractice.com/index.php")
women_tab = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
click_element_by_xpath(women_tab)
go_bac_previous_page()
refresh_browser()
go_next_page()
close_browser()

# Scenario: Login to automationpractice.com
# Prerequisite: create and account:
# username: abdu@email.com, have strong password: "123456789"
launch_website("http://automationpractice.com/index.php")
# identify all locators
sign_in_link = "//a[@class='login']"
email_input = "//input[@id='email']"
password_input = "//input[@id='passwd']"

