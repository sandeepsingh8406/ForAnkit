from asyncore import loop
from Pre import *
Scenario = "ankit"
launchpath(Scenario+"1")
login(Scenario+"1")
expand_sales_download()
for i in range(1,8):
    print(i)
    if i>1:
        launchpath(Scenario+"1")
        login(Scenario+"1")
        expand_sales_download()
    setsalereportparameter(Scenario+str(i))
    newtab()

#Step 1
# launchpath(Scenario)
# login(Scenario)

# #Step 2
# expand_sales_download()
# setsalereportparameter(Scenario)
input()