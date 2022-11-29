import pytest
from selenium import webdriver
from Library.config import Config
# path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options

#Cross Browsing
Firefox_Driver_Path = r"C:\Users\DELL\Desktop\driver_\geckodriver.exe"
@pytest.fixture(params=["Firefox","Edge","Chrome"])
def _driver(request):




    if request.param == "Firefox":
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=Firefox_Driver_Path,options=options)


    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_Driver_Path)



    elif request.param == "Chrome":
        driver = webdriver.Chrome(Config.ChromePath_Driver_Path)



    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(60)
    yield driver
    print(driver.title)
    # driver.save_screenshot("text_loginpage.png")
    driver.close()