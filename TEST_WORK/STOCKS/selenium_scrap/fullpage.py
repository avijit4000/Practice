from selenium import webdriver
import pandas as pd
from selenium.webdriver.edge.options import Options
import time
# df=pd.read_csv(r"D:\Pyn\online learning\FINAL_DATA\SCRNER_DATA\onlynifty500.csv")
# n=len(df["company_url"])
# print(n)
# print(df["company_url"][n-1])
# for i in df["company_url"]:
#     print(i)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
driver.get("https://www.screener.in/login/?")
# driver.maximize_window()
username = driver.find_element("xpath",'//input[@name="username"]')
username.send_keys("avijit4000@gmail.com")
passward = driver.find_element("xpath",'//input[@name="password"]')
passward.send_keys("Biswas.123")
button = driver.find_element("xpath",'//button[@class="button-primary"]')
button.click()
driver.get("https://www.screener.in/company/TATASTEEL")
table1 = driver.find_element("xpath", '//section[@class="card card-large"][4]/div[3]/table/tbody/tr[1]/td')
n=len(table1)
print(n)
# Market_cap.append(table.find_element("xpath", './/li[1]/span[2]/span').text)
a=[]
for i in range(1,n-1):
    a.append(table1.find_element("xpath", f'.//[{i}]').text)
print(a)