from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
path = r'C:\Users\DELL\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
# driver.get("https://www.abhibus.com/")
# driver.maximize_window()
from Data.reading_objects import ReadExcel
from Library.config import Config
read_xl = ReadExcel()

from Data import reading_objects
Trains = read_xl.read_locators(Config.read_locators)


class Trains1:
    def __init__(self,driver):
        self.driver = driver
    def openTrainspage(self):
        self.driver.find_element(*Trains["open_Trainspage"]).click()
        driver.implicitly_wait(30)
    def forSource(self,forsource_):
        source = self.driver.find_element(*Trains["for_click"])
        source.click()
        from_ = self.driver.find_element(*Trains['source_click'])
        from_.send_keys(forsource_)
        self.driver.find_element(*Trains["from_click"]).click()
        time.sleep(2)
    def forDestination(self,fordestination_):
        destn_ = self.driver.find_element(*Trains["for_destination"])
        destn_.click()
        to_ = self.driver.find_element(*Trains["destination_click"])
        to_.send_keys(fordestination_)
        self.driver.find_element(*Trains["to_click"]).click()
        time.sleep(2)

    def forSearch(self):
        self.driver.find_element(*Trains["for_search"]).click()
        time.sleep(5)
    def forCalendar(self):
        self.driver.find_element(*Trains["for_calendar"]).click()
        time.sleep(3)
        self.driver.find_element(*Trains["calendar_btn"]).click()
        time.sleep(3)
        self.driver.find_element(*Trains["calendar_date"]).click()
        time.sleep(3)
    def Trainindex(self):
        self.driver.find_element(*Trains["select_Train_index"]).click()
        time.sleep(2)
    def Mobilenumber(self,mobile_number):
        self.driver.find_element(*Trains["for_mobilenumber"]).send_keys(mobile_number)
        time.sleep(5)
    def Generateotp(self):
        self.driver.find_element(*Trains["for_generate_otp"]).click()
        time.sleep(30)
    def Submitotp(self):
        self.driver.find_element(*Trains["for_submit_otp"]).click()
        time.sleep(2)
    def bookingtrain(self):
        self.driver.find_element(*Trains["select_train_6days_index"]).click()
        time.sleep(2)
        self.driver.find_element(*Trains["select_train"]).click()
        time.sleep(2)
    def Irctcuserid(self,irctc_id):
        self.driver.find_element(*Trains["for_irctc_userid"]).send_keys(irctc_id)
        time.sleep(2)
    def Proceed(self):
        self.driver.find_element(*Trains["for_proceed"]).click()
        time.sleep(2)

# result=Trains(driver)
# result.openTrainspage()
# result.forSource()
# result.forDestination()
# result.forSearch()
# result.forCalendar()
# result.Trainindex()
# result.Mobilenumber()
# result.Generateotp()
# result.Submitotp()
# result.bookingtrain()
# result.Irctcuserid()
# result.Proceed()





