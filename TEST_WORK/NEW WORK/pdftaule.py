# import camelot
#
# # Extract tables from the PDF
# tables = camelot.read_pdf('Book1.pdf')
#
# # Print the number of tables extracted
# print(f'Total tables extracted: {len(tables)}')
#
# # Iterate through tables and print each table
# for i, table in enumerate(tables):
#     print(f'Table {i+1}:')
#     print(table.df)  # table.df is a DataFrame
import tabula

# Extract tables from the PDF
tables = tabula.read_pdf('Book1.pdf', pages='all', multiple_tables=True)

# Print the number of tables extracted
print(f'Total tables extracted: {len(tables)}')

# Iterate through tables and print each table
for i, table in enumerate(tables):
    print(f'Table {i+1}:')
    print(table)  # Each table is a DataFrame

