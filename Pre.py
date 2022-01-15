import time
import Paths
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import ExcelLoad
driver = webdriver.Chrome(os.getcwd()+"\Resources\chromedriver.exe")
driver.maximize_window()
def wait(int):
    time.sleep(int)

def launchpath(Scenario):
    URL = ExcelLoad.TestData(Scenario,"Url")
    print("My data: ",URL)
    driver.get(URL)

def click(element):
    driver.find_element_by_xpath(element).click()

def setvalue(element, value):
    driver.find_element_by_xpath(element).send_keys(value)

def valueclear(element):
    driver.find_element_by_xpath(element).clear()

def setdate(element, date):
    click(element)
    valueclear(element)
    setvalue(element, date)

def login(Scenario):
    setvalue(Paths.username, ExcelLoad.TestData(Scenario,"Username"))
    setvalue(Paths.password, ExcelLoad.TestData(Scenario,"Password"))
    driver.implicitly_wait(2)
    click(Paths.signin)
    driver.implicitly_wait(5)

def expand_sales_download():
    click(Paths.download_expand)
    click(Paths.sales_download)

def set_drop_down(element, value):
    click(element)
    click(Paths.valueselect(value))

def setsalereportparameter(Scenario):
    driver.implicitly_wait(5)
    set_drop_down(Paths.Region, ExcelLoad.TestData(Scenario,"Region"))
    set_drop_down(Paths.Level, ExcelLoad.TestData(Scenario,"Level"))
    set_drop_down(Paths.Application, ExcelLoad.TestData(Scenario,"Application"))
    set_drop_down(Paths.Location, ExcelLoad.TestData(Scenario,"Location"))
    setdate(Paths.datefrom, ExcelLoad.TestData(Scenario,"Fromdate"))
    setdate(Paths.dateto, ExcelLoad.TestData(Scenario,"Todate"))
    click(Paths.Submit_Report)
def newtab():
    driver.execute_script("window.open('');")


