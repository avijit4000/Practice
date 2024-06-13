# print("Avijti")
# import PyPDF2
# # a=PyPDF2.PdfFileReader("Book1.pdf")
# # print(a.documentInfo)
# file=open("Book1.pdf","rb")
# reader=PyPDF2.PdfFileReader(file)
# page1=reader.getPage(0)
# print(reader.numPages)
# pdfdata=page1.extract_text()
# print(pdfdata)
# from PyPDF2 import PdfFileReader
#
# with open('Book1.pdf', 'rb') as file:
#     reader = PdfFileReader(file)
#     number_of_pages = reader.getNumPages()
#     first_page = reader.getPage(0)
#     text = first_page.extract_text()
#     print(text)
from PyPDF2 import PdfReader
da1=[]
with open('New Invoice last July.pdf', 'rb') as file:
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    for i in range(number_of_pages):
        first_page = reader.pages[i]
        text = first_page.extract_text()
        da1.append(text)
        print(text)

with open("output1.txt", 'w') as file:
    # Iterate through the list and write each element to the file
    for item in da1:
        file.write(f"{item}\n")
