"""
A simple cookbook for interactions with Microsoft Excel files (Better off converting them to .csv but if you insist...)
"""

import openpyxl


# Make new workbook
wb = openpyxl.Workbook()
# Target active sheet for read/write
sheet = wb.active
# Give the sheet a title
sheet.title = 'Report #1'

# Save workbook
wb.save(f'My_Excel_File.xlsx')

# Returns the highest numbered row that contains data. use +1 to auto move to the nearest blank row
nearest_blank_row = sheet.max_row + 1 

# Write value to the nearest blank row
sheet[f'A{nearest_blank_row}'].value = 'Example column A value'

# Automate header information
# These are our desired header details:
headers = ['Site Name', 'Site ID', 'Status', 'IPv4', 'Original DNS', 'Active',
           'WAF', 'Bot Control', 'DDoS', 'Custom Cert', 'Cert SAN', 'Validation',
           'Performance', 'Custom Rules']
# Iterate through the headers and apply them in order to cells in the 1st row
for x in range(len(headers)):
  # Header is the string value
	header = headers[x]
  # Letter is the column in which the header will go
	letter = string.ascii_uppercase[x]
  # [letter+str(1)] is equal to A1, B1 etc.
  # .value = header makes that column header the string value within headers[]
	sheet[letter+str(1)].value = header

# Freeze panes leaving the header and column A static!
sheet.freeze_panes = sheet['B2']

# Auto-adjust dimensions to fit cell data
dimensions = {}
for row in sheet.rows:
    for cell in row:
        if cell.value:
            dimensions[cell.column_letter] = max((dimensions.get(cell.column_letter, 0), len(str(cell.value))))     
for col, value in dimensions.items():
    sheet.column_dimensions[col].width = value
    
# Save workbook
wb.save(f'My_Excel_File.xlsx')


# TODO: open and ingest xlsx file data
