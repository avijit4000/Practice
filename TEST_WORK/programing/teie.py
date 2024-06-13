from selenium import webdriver
import pandas as pd
from selenium.webdriver.edge.options import Options


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
driver.maximize_window()
y=driver.get("https://www.forbes.com/lists/hong-kong-billionaires/?sh=10acbf906495")


e=[]
f=[]
g=[]


u=driver.find_elements("xpath",'//div[@class="personName second table-cell    name"]')
v=driver.find_elements("xpath",'//div[@class="finalWorth  table-cell    net worth ($)"]')
w=driver.find_elements("xpath",'//div[@class="category  table-cell    industry"]')
for i in u:
    e.append(i.text)
for j in v:
    f.append(j.text)
for k in w:
    g.append(k.text)
df = pd.DataFrame({'name':e, 'wroth': f, 'fild': g})
print(df)
df.to_csv('bile.csv',index=False)
driver.quit()