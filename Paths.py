username = "//input[@type='email']"
password = "//input[@type='password']"
signin = "//button[@type='submit']"
download_expand = "(//i[@class='fas fa-angle-left right'])[5]"
sales_download = "//a[@href='https://drop52.reports.cloware.com/downloads/page/sales_datadownload']"

#Download Report
Region = "(//b[@role='presentation'])[1]"
Level = "(//b[@role='presentation'])[2]"
Application = "(//b[@role='presentation'])[3]"
Location = "(//b[@role='presentation'])[4]"
Submit_Report = "//button[@class='btn btn-primary btn-sm btn-flat']"
datefrom = "//input[@id='filter1']"
dateto = "//input[@id='filter2']"
valuetoselect = "//li[text()='{o}']"

def valueselect(value):
    value1 = valuetoselect.replace('{o}',value)
    return value1

#DMS Login

DMS_signin = "//input[@class='login_bt' and @type='submit']"
DMS_password = "//input[@class='input_text' and @type='password']"
DMS_username = "//input[@class='input_text' and @type='text']"