from behave import *
from selenium import webdriver
import time


# @given(u'open the chrome browser')
# def step_impl(context):
#     path = r'C:\Users\DELL\Downloads\chromedriver_win32\chromedriver.exe'
#     context.driver = webdriver.Chrome(path)
#
#
# @when(u'Enter the URL')
# def step_impl(context):
#     context.driver.get("https://www.abhibus.com/")
#
# @then(u'click on the Train Icon')
# def step_impl(context):
#     context.driver.find_element_by_xpath("//a[@class='nav-link bg-gray  rounded-pill px-4 py-1']").click()
#
#
# @then(u'click on "From" text field')
# def step_impl(context):
#     source = context.driver.find_element_by_xpath('//div[@class="source"]//div[@class="label-container"]')
#     source.click()
#
# @then(u'Enter the cityname in Fromserch')
# def step_impl(context):
#     from_ = context.driver.find_element("xpath", '//input[@placeholder="Enter from"]')
#     from_.send_keys("pune")
#
#
# @then(u'it will select that particular city')
# def step_impl(context):
#     context.driver.find_element("xpath", '//li[@id="source-item-4"]').click()
#
#
# @then(u'click on "To" text field')
# def step_impl(context):
#     destn_ = context.driver.find_element_by_xpath('//div[@class="destination"]//div[@class="label-container"]')
#     destn_.click()
#
#
# @then(u'Enter the city name in Tosearch')
# def step_impl(context):
#     to_ = context.driver.find_element("xpath", '//input[@placeholder="Enter to"]')
#     to_.send_keys("bangalore")
#
#
# @then(u'it will select the particular city')
# def step_impl(context):
#     context.driver.find_element("xpath", '//li[@id="destination-item-3"]').click()
#
#
# @then(u'click on "Searchbutton"')
# def step_impl(context):
#     context.driver.find_element("xpath","//span[text()='SEARCH']").click()
#
#
# @then(u'click on "DateofJourney"')
# def step_impl(context):
#     context.driver.find_element("xpath", "//i[text()='calendar_today']").click()
#
# @then(u'select the month')
# def step_impl(context):
#     context.driver.find_element("xpath",'//button[@class="MuiButtonBase-root MuiIconButton-root MuiPickersCalendarHeader-iconButton"]').click()
#
#
# @then(u'select the Date')
# def step_impl(context):
#     context.driver.find_element("xpath","//p[text()='8']").click()
#
# @then(u'Click the particular train')
# def step_impl(context):
#     context.driver.find_element("xpath","(//span[text()='SL'])[1]").click()
#
#
# @then(u'Enter the Mobile number')
# def step_impl(context):
#     context.driver.find_element("xpath", "//input[@id='mobile-number']").send_keys('9059455838')
#
#
# @then(u'Enter the given OTP')
# def step_impl(context):
#     context.driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
#
#
# @then(u'Now click on submit button')
# def step_impl(context):
#     context.driver.find_element("xpath","//span[@class='MuiButton-label']").click()
#
#
# @then(u'Click on checkavailabity')
# def step_impl(context):
#     context.driver.find_element("xpath","(//div[@class='check-six-days'])[4]").click()
#
#
# @then(u'select the train')
# def step_impl(context):
#     context.driver.find_element("xpath","(//div[@class='book-btn p'])[1]").click()
#
#
# @then(u'Enter the IRCTC user id')
# def step_impl(context):
#     context.driver.find_element("xpath","//input[@class='MuiInputBase-input MuiInput-input']").send_keys("sravanivadithya")
#
#
# @then(u'Click on proceed button')
# def step_impl(context):
#     context.driver.find_element("xpath","//span[text()='PROCEED']").click()
#
@given(u'open the chrome browser')
def step_impl(context):
    path = r'C:\Users\DELL\Downloads\chromedriver_win32\chromedriver.exe'
    context.driver = webdriver.Chrome(path)

@when(u'Enter the URL')
def step_impl(context):
    context.driver.get("https://www.abhibus.com/")
    context.driver.maximize_window()

@then(u'click on the Train Icon')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@class='nav-link bg-gray  rounded-pill px-4 py-1']").click()
    context.driver.implicitly_wait(10)


@given(u'click on "From" text field')
def step_impl(context):
    source = context.driver.find_element_by_xpath('//div[@class="source"]//div[@class="label-container"]')
    source.click()


@when(u'Enter the cityname in Fromserch')
def step_impl(context):
    from_ = context.driver.find_element("xpath", '//input[@placeholder="Enter from"]')
    from_.send_keys("pune")

@then(u'it will select that particular city')
def step_impl(context):
    context.driver.find_element("xpath", '//li[@id="source-item-4"]').click()


@then(u'click on "To" text field')
def step_impl(context):
    destn_ = context.driver.find_element_by_xpath('//div[@class="destination"]//div[@class="label-container"]')
    destn_.click()


@then(u'Enter the city name in Tosearch')
def step_impl(context):
    to_ = context.driver.find_element("xpath", '//input[@placeholder="Enter to"]')
    to_.send_keys("bangalore")

@then(u'it will select the particular city')
def step_impl(context):
    context.driver.find_element("xpath", '//li[@id="destination-item-3"]').click()


@then(u'click on "Searchbutton"')
def step_impl(context):
    context.driver.find_element("xpath","//span[text()='SEARCH']").click()

@then(u'click on "DateofJourney"')
def step_impl(context):
    context.driver.find_element("xpath","//i[text()='calendar_today']").click()
    time.sleep(2)

@then(u'select the month')
def step_impl(context):
    context.driver.find_element("xpath",'//button[@class="MuiButtonBase-root MuiIconButton-root MuiPickersCalendarHeader-iconButton"]').click()
    time.sleep(2)

@then(u'select the Date')
def step_impl(context):
    context.driver.find_element("xpath","//p[text()='8']").click()
    time.sleep(2)

@then(u'Click the particular train')
def step_impl(context):
    context.driver.find_element("xpath","(//span[text()='SL'])[1]").click()
    time.sleep(2)

@then(u'Enter the Mobile number')
def step_impl(context):
    context.driver.find_element("xpath","//input[@id='mobile-number']").send_keys('7776988991')

@then(u'Enter the given OTP')
def step_impl(context):
    context.driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
    time.sleep(30)

@then(u'Now click on submit button')
def step_impl(context):
    context.driver.find_element("xpath","//span[@class='MuiButton-label']").click()
    time.sleep(2)

@then(u'Click on checkavailabity')
def step_impl(context):
    context.driver.find_element("xpath","(//div[@class='check-six-days'])[1]").click()
    time.sleep(2)


@then(u'select the train')
def step_impl(context):
    context.driver.find_element("xpath","(//div[@class='book-btn p'])[1]").click()
    time.sleep(2)

@then(u'Enter the IRCTC user id')
def step_impl(context):
   context.driver.find_element("xpath","//input[@class='MuiInputBase-input MuiInput-input']").send_keys("sravanivadithya")
   time.sleep(2)

@then(u'Click on proceed button')
def step_impl(context):
    context.driver.find_element("xpath","//span[text()='PROCEED']").click()

