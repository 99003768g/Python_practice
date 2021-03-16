# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = "example.xls"

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# word = "r2c2"
word = input("enter the word to be found: ")
print("you entered right????????")
# For row 0 and column 0
'''
for i in sheet:
    for j in sheet:
        if sheet.value == "r2c2":
            # word == sheet.cell_value(i, j):
            print("found hurrahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", i, j)
        else:
            print("not found")
# print(sheet.cell_value(0, 1))
# print(sheet.cell_value(2, 2))
# print(sheet.cell_value(3, 3))
'''
for sh in xlrd.open_workbook(loc).sheets():
    for row in range(sh.nrows):
        for col in range(sh.ncols):
            myCell = sh.cell(row, col)
            # print(myCell)
            if myCell.value == word:
                print('-----------')
                print('Found! hurrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
                # print(xl_rowcol_to_cell(row,col))
                # quit()


