from Pre import *
Scenario = "Sales_Report_Download"

#Step 1
launchpath(Scenario)
login(Scenario)

#Step 2
expand_sales_download()
setsalereportparameter(Scenario)