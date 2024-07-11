from selenium import webdriver
import pandas as pd
from selenium.webdriver.edge.options import Options
import time

company_list=pd.read_csv(r"D:\Pyn\online learning\INURAN_DATA\FSDS_September\TEST_WORK\STOCKS\scrneer\type_of_company.csv")
n=len(company_list["link"])
print(n)
# for i in company_list["link"]:
#     print(i)

# print(company_list["link"][1])

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)

driver.get("https://www.screener.in/login/?")
driver.maximize_window()


username = driver.find_element("xpath",'//input[@name="username"]')
username.send_keys("avijit4000@gmail.com")

passward = driver.find_element("xpath",'//input[@name="password"]')
passward.send_keys("Biswas.123")


button = driver.find_element("xpath",'//button[@class="button-primary"]')
button.click()

type_of_company=[]
company_name = []
company_link = []


for j in range(n):
    link=company_list["link"][j]
    time.sleep(3)
    # link = "https://www.screener.in/company/compare/00000001/"
    driver.get(link)
    # table = driver.find_elements("xpath", '//table[@class="data-table text-nowrap striped mark-visited"]/tbody/tr')

    next_list = driver.find_elements("xpath",
                                     '//div[@class="flex-row flex-space-between margin-top-16 margin-bottom-36"]/div')



    if len(next_list) == 2:
        pipa = next_list[1].find_elements("xpath", './/a')
        n = len(pipa)

        for i in range(n):
            time.sleep(2)
            driver.get(f"{link}?page={i + 1}")  # Increment page number

            table_rows = driver.find_elements("xpath",
                                              '//table[@class="data-table text-nowrap striped mark-visited"]/tbody/tr/td[2]')

            for row in table_rows:
                type_of_company.append(driver.find_element("xpath", '//h1').text)
                company_name.append(row.text)
                company_link.append(row.find_element("xpath",'.//a').get_attribute('href'))

    else:

        table_rows = driver.find_elements("xpath",
                                          '//table[@class="data-table text-nowrap striped mark-visited"]/tbody/tr/td[2]')
        for row in table_rows:
            type_of_company.append(driver.find_element("xpath", '//h1').text)
            company_name.append(row.text)
            company_link.append(row.find_element("xpath", './/a').get_attribute('href'))


com = pd.DataFrame({"type_of_company": type_of_company, "company_name": company_name, "company_url": company_link})
com.to_csv("D:\Pyn\online learning\INURAN_DATA\FSDS_September\TEST_WORK\STOCKS\FINAL_DATA\SCRNER_DATA\download_data\companynamewithlist_2.csv", index=False)

driver.quit()











# link="https://www.screener.in/company/compare/00000009/"
# driver.get(link)
# table=driver.find_elements("xpath",'//table[@class="data-table text-nowrap striped mark-visited"]/tbody/tr')
#
# next_list=driver.find_elements("xpath",'//div[@class="flex-row flex-space-between margin-top-16 margin-bottom-36"]/div')
# # print(len(next_list))
# company_name=[]
# company_link=[]
# if len(next_list)==2:
#     pipa=next_list[1].find_elements("xpath",'.//a')
#     n=len(pipa)
#     for i in range(1,n+1):
#         time.sleep(2)
#         driver.get(f"{link}?page={i}")
#         table = driver.find_element("xpath", '//table[@class="data-table text-nowrap striped mark-visited"]/tbody/tr/td[2]')
#         company_name.append(table.text)
#         company_link.append(table.get_attribute('href'))
# else:
#     print('not ok')
# com=pd.DataFrame({"company_name": company_name, "company_link":company_link})
# com.to_csv("companynamelist1.csv",index=False)
#     (next_list[len(next_list)-1].text)=="Next"
#
#     print('I am comeing')
# else:
#     print('some thing wrong')
# print(len(next_list))
# print(next_list[len(next_list)-1].text)
# for i in next_list:
#     print(i.text)



# driver.quit()