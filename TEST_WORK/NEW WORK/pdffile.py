
# # Read pdf into a list of DataFrame
# dfs = tabula.read_pdf("New Invoice last July.pdf", pages='all')
import re
# from pdfminer.high_level import extract_pages, extract_text
# for page_layout in extract_pages("New Invoice last July.pdf"):
#     for element in page_layout:
#         print(element)
#
# import camelot
# tables = camelot.read_pdf('foo.pdf')
# tables
# pip install tabula-py
# import tabula
#
# # Read tables from the PDF file
# tables = tabula.read_pdf("Book1.pdf", pages="all")

# # Print the tables
# for i, table in enumerate(tables):
#     print(f"Table {i + 1}")
#     print(table)
#     print("\n")
import tabula

# Read tables from the PDF file
tables = tabula.read_pdf("Book1.pdf", pages="all")

# Print the tables
for i, table in enumerate(tables):
    print(f"Table {i + 1}")
    print(table)
    print("\n")


