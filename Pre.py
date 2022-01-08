import time
import Paths
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("D:\drivers\Resources\chromedriver.exe")
def wait(int):
    time.sleep(int)

def launchpath(URL):
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

def login(username, password):
    setvalue(Paths.username, username)
    setvalue(Paths.password, password)
    driver.implicitly_wait(2)
    click(Paths.signin)
    driver.implicitly_wait(5)

def expand_sales_download():
    click(Paths.download_expand)
    click(Paths.sales_download)

def set_drop_down(element, value):
    click(element)
    click(Paths.valueselect(value))

def setsalereportparameter(Region, Level, Application, Location, FromDate, ToDate):
    driver.implicitly_wait(5)
    set_drop_down(Paths.Region, Region)
    set_drop_down(Paths.Level, Level)
    set_drop_down(Paths.Application, Application)
    set_drop_down(Paths.Location, Location)
    setdate(Paths.datefrom, FromDate)
    setdate(Paths.dateto, ToDate)
    click(Paths.Submit_Report)



