from Pre import *
#Inputs----------------------------------------------------------
Path = "https://drop52.reports.cloware.com/reports/page/dashboard"
username = "reportsadmin@drop52.cloware.com"
password = "Reports@3961"
Region="CHANDIGARH BRANCH"
Level = "Town(WD)"
Application = "Select"
Location = "Select"
FromDate = "01-01-2022"
ToDate = "07-01-2022"

#----------------------------------------------------------------
#Step 1
launchpath(Path)
login(username,password)

#Step 2
expand_sales_download()
setsalereportparameter(Region, Level, Application, Location, FromDate, ToDate)



