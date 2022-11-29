from selenium import webdriver
#from selenium.webdriver.support.select import Select
import time
path = r'C:\Users\DELL\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://www.abhibus.com/")
driver.maximize_window()
time.sleep(2)
#open trainspage
driver.find_element_by_xpath("//a[@class='nav-link bg-gray  rounded-pill px-4 py-1']").click()
driver.implicitly_wait(10)
# for source
source = driver.find_element_by_xpath('//div[@class="source"]//div[@class="label-container"]')
source.click()
from_ = driver.find_element("xpath", '//input[@placeholder="Enter from"]')
from_.send_keys("pune")
driver.find_element("xpath", '//li[@id="source-item-4"]').click()
# "source-item-3" the number 3 is according to index
# if u want anything in particular check the index

# for destination
destn_ = driver.find_element_by_xpath('//div[@class="destination"]//div[@class="label-container"]')
destn_.click()
to_ = driver.find_element("xpath",'//input[@placeholder="Enter to"]')
to_.send_keys("bangalore")
driver.find_element("xpath", '//li[@id="destination-item-3"]').click()


#for search
driver.find_element("xpath","//span[text()='SEARCH']").click()
time.sleep(2)

#for calendar
driver.find_element("xpath","//i[text()='calendar_today']").click()
time.sleep(3)
driver.find_element("xpath",'//button[@class="MuiButtonBase-root MuiIconButton-root MuiPickersCalendarHeader-iconButton"]').click()
time.sleep(2)
driver.find_element("xpath","//p[text()='8']").click()
time.sleep(2)

#selecting train index
driver.find_element("xpath","(//span[text()='SL'])[1]").click()
time.sleep(2)

#for mobilenumber
driver.find_element("xpath","//input[@id='mobile-number']").send_keys('8374713245')
time.sleep(5)

#for generate otp
driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
time.sleep(30)

#for submit otp
driver.find_element("xpath","//span[@class='MuiButton-label']").click()
time.sleep(2)

#for search train for booking
driver.find_element("xpath","(//div[@class='check-six-days'])[1]").click()
# driver.find_element("xpath","(//div[@class='check-six-days'])[2]").click()
time.sleep(2)
driver.find_element("xpath","(//div[@class='book-btn p'])[1]").click()
time.sleep(2)

#for irctc userid
driver.find_element("xpath","//input[@class='MuiInputBase-input MuiInput-input']").send_keys("sravanivadithya")
time.sleep(2)

#for proceed
driver.find_element("xpath","//span[text()='PROCEED']").click()
time.sleep(2)

# #for passenger details
# driver.find_element("xpath","//input[@value="F"]").click()
# # driver.find_element_by_xpath("(//span[text()='3A'])[1]").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@id='passengerName']").send_keys("Muragandlachandini")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='passengerAge']").send_keys("21")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='email']").send_keys("chandinimuragandla838@gmail.com")
# time.sleep(2)
# driver.find_element("xpath","//div[text()='PROCEED']").click()
