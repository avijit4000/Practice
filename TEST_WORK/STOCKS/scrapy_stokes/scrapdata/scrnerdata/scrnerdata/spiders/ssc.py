import scrapy
import re
import csv


class SscSpider(scrapy.Spider):
    name = "ssc"
    allowed_domains = ["www.screener.in"]
    # start_urls = ["http://www.screener.in/company/TATASTEEL/"]

    def __init__(self, *args, **kwargs):
        super(SscSpider, self).__init__(*args, **kwargs)

        # Define the path to the CSV file
        file_path = r'D:\Pyn\online learning\INURAN_DATA\FSDS_September\TEST_WORK\STOCKS\FINAL_DATA\SCRNER_DATA\download_data\all_companysdata.csv'

        # Initialize the start_urls list
        self.start_urls = []

        # Open the CSV file
        with open(file_path, mode='r', newline='') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)

            # Get the header row
            header = next(csv_reader)

            # Find the index of the "Company_link" column
            company_link_index = header.index("Company_link")

            # Read the "Company_link" column from each row and add to start_urls
            for row in csv_reader:
                self.start_urls.append(row[company_link_index])


    def parse(self, response):
        company_name=response.xpath("//*[@id='top']/div[1]/div/h1/text()").get()
        arti = response.xpath("//*[@id='top-ratios']/li")
        for i in arti:
            name = i.xpath(".//span[1]/text()").get()
            value = i.xpath(".//span[2]/span/text()").get()
            if name:
                name = re.sub(r'\s+', ' ', name).strip()
            if value:
                value = re.sub(r'\s+', ' ', value).strip()
            yield {
                "company_name" : company_name,
                name: value
            }
# quarterly results

        data = response.xpath("//*[@id='quarters']/div[3]/table/tbody/tr")
        for j in data:
            if j.xpath(".//td[1]/button"):
                name1 = j.xpath(".//td[1]/button/text()").get()
            else:
                name1 = j.xpath(".//td[1]/text()").get()

            # Ensure name1 is not None and strip it of extra whitespace
            if name1:
                name1 = name1.strip()

            # Extract values from the remaining td elements, ignoring the first one
            values = j.xpath(".//td[position() > 1]/text()").getall()
            values = [value.strip() for value in values if value.strip()]

            yield {
                name1: values
            }
## profit loss
        data1 = response.xpath("//*[@id='profit-loss']/div[3]/table/tbody/tr")
        for j in data1:
            if j.xpath(".//td[1]/button"):
                name1 = j.xpath(".//td[1]/button/text()").get()
            else:
                name1 = j.xpath(".//td[1]/text()").get()

            # Ensure name1 is not None and strip it of extra whitespace
            if name1:
                name1 = name1.strip()

            # Extract values from the remaining td elements, ignoring the first one
            values = j.xpath(".//td[position() > 1]/text()").getall()
            values = [value.strip() for value in values if value.strip()]

            yield {
                name1: values
            }

        #Balance sheet
        data2 = response.xpath("//*[@id='balance-sheet']/div[2]/table/tbody/tr")
        for j in data2:
            if j.xpath(".//td[1]/button"):
                name1 = j.xpath(".//td[1]/button/text()").get()
            else:
                name1 = j.xpath(".//td[1]/text()").get()

            # Ensure name1 is not None and strip it of extra whitespace
            if name1:
                name1 = name1.strip()

            # Extract values from the remaining td elements, ignoring the first one
            values = j.xpath(".//td[position() > 1]/text()").getall()
            values = [value.strip() for value in values if value.strip()]

            yield {
                name1: values
            }

        # Cash flow:
        data3 = response.xpath("//*[@id='cash-flow']/div[2]/table/tbody/tr")
        for j in data3:
            if j.xpath(".//td[1]/button"):
                name1 = j.xpath(".//td[1]/button/text()").get()
            else:
                name1 = j.xpath(".//td[1]/text()").get()

            # Ensure name1 is not None and strip it of extra whitespace
            if name1:
                name1 = name1.strip()

            # Extract values from the remaining td elements, ignoring the first one
            values = j.xpath(".//td[position() > 1]/text()").getall()
            values = [value.strip() for value in values if value.strip()]

            yield {
                name1: values
            }
        # Ratios:
        data4 = response.xpath("//*[@id='ratios']/div[2]/table/tbody/tr")
        for j in data4:
            if j.xpath(".//td[1]/button"):
                name1 = j.xpath(".//td[1]/button/text()").get()
            else:
                name1 = j.xpath(".//td[1]/text()").get()

            # Ensure name1 is not None and strip it of extra whitespace
            if name1:
                name1 = name1.strip()

            # Extract values from the remaining td elements, ignoring the first one
            values = j.xpath(".//td[position() > 1]/text()").getall()
            values = [value.strip() for value in values if value.strip()]

            yield {
                name1: values
            }
        # share holding patter
        data5 = response.xpath("//*[@id='quarterly-shp']/div/table/tbody/tr")
        for j in data5:
            if j.xpath(".//td[1]/button"):
                name1 = j.xpath(".//td[1]/button/text()").get()
            else:
                name1 = j.xpath(".//td[1]/text()").get()

            # Ensure name1 is not None and strip it of extra whitespace
            if name1:
                name1 = name1.strip()

            # Extract values from the remaining td elements, ignoring the first one
            values = j.xpath(".//td[position() > 1]/text()").getall()
            values = [value.strip() for value in values if value.strip()]

            yield {
                name1: values
            }
