
# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = "example.xls"

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

word = "r2c2"
#    input("enter the word to be found: ")
print("you entered right????????")
# For row 0 and column 0
# for i in sheet:
#    for j in sheet:
if word == sheet.cell_value(2, 2):
    print("found hurrahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
else:
    print("not found")
# print(sheet.cell_value(0, 1))
# print(sheet.cell_value(2, 2))
# print(sheet.cell_value(3, 3))
