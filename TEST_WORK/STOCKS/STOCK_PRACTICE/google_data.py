from bs4 import BeautifulSoup as bs
import requests as re
import pandas as pd
import yfinance as yf
import numpy as np
con = re.get('https://www.google.com/finance/markets/gainers?authuser=0').text
soup = bs(con,'lxml')
box = soup.find_all("li")
ticket=[]
name = []
price = []
increase = []
pseincre = []
for i in box:
    ticket.append(i.find("div" , class_="COaKTb").text)
    name.append(i.find("div" , class_="ZvmM7").text)
    price.append(i.find("div" , class_="YMlKec").text)
    increase.append(i.find("span" , class_="P2Luy Ez2Ioe").text)
    pseincre.append(i.find("div" , class_="JwB6zf").text)
df = pd.DataFrame({"ticket" : ticket,"name" : name , "price" : price , "increase" : increase , "pseincre" : pseincre})

df['price']=df['price'].str.split("₹").str[1]
# df['price']=df['price'].replace(",","")
df['price']=df['price'].str.replace(",","")
df['price']=df['price'].astype(float)

df['increase']=df['increase'].str.split("₹").str[1]
df['increase']=df['increase'].astype(float)

df['pseincre']=df['pseincre'].str.split("%").str[0]
df['pseincre']=df['pseincre'].astype(float)

p=[]
for i in df.ticket:
    p.append(i+".NS")

df_sh={}
for i in p:
    df_sh[i] = yf.download(f"{i}", start="2010-11-11", end="2023-12-10", interval="1d")
for j in df_sh.keys():
    df_sh[j]['Daily_Return'] = df_sh[j]['Close'].pct_change()
for k in df_sh.keys():
    k = df_sh[k]['Daily_Return'].resample('M').apply(lambda x: (x + 1).prod() - 1)

print(df_sh.keys())



# print(df.head(5))
# print(df.info())
# print(p)
monthly_returns= df_sh["CHEVIOT.NS"]['Daily_Return'].resample('M').apply(lambda x: (x + 1).prod() - 1)
monthly_returns=monthly_returns.apply(lambda x:x*100)
monthly_returns=monthly_returns.round(2)
monthly_returns.sort_values(ascending=False)

