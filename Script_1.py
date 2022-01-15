from asyncore import loop
from Pre import *
Scenario = "ankit"
launchpath(Scenario+"1")
login(Scenario+"1")
expand_sales_download()
for i in range(1,8):
    print(i)
    if i>1:
        newtab(i-1)
        launchpath(Scenario+str(i))
        expand_sales_download()
    setsalereportparameter(Scenario+str(i))
input()