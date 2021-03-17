import pandas as pd
from openpyxl import load_workbook

excel_file = pd.ExcelFile('sample.xlsx')

df_mini_first_sheet = pd.read_excel(excel_file, sheet_name=0)
df_mini_second_sheet = pd.read_excel(excel_file, sheet_name=1)
df_mini_third_sheet = pd.read_excel(excel_file, sheet_name=2)
df_mini_fourth_sheet = pd.read_excel(excel_file, sheet_name=3)
df_mini_fifth_sheet = pd.read_excel(excel_file, sheet_name=4)

file3 = df_mini_first_sheet.merge(df_mini_second_sheet, on="segment", how="left")
file4 = file3.merge(df_mini_third_sheet, on="segment", how="left")
file5 = file4.merge(df_mini_fourth_sheet, on="segment", how="left")
file6 = file5.merge(df_mini_fifth_sheet, on="segment", how="left")

Input = input("Enter Segment: ")

df_Input = pd.DataFrame(file6, columns=['segment', 'country1','product1', 'band1', 'sold1', 'price1', 'sale1', 'discount1', 'sales1', 'cogs1', 'profit1', 'done1', 'date1', 'month1', 'name1', 'year1'
                                        , 'country2','product2', 'band2', 'sold2', 'price2', 'sale2', 'discount2', 'sales2', 'cogs2', 'profit2', 'done2', 'date2', 'month2', 'name2', 'year2'
                                        , 'country3','product3', 'band3', 'sold3', 'price3', 'sale3', 'discount3', 'sales3', 'cogs3', 'profit3', 'done3', 'date3', 'month3', 'name3', 'year3'
                                        , 'country4','product4', 'band4', 'sold4', 'price4', 'sale4', 'discount4', 'sales4', 'cogs4', 'profit4', 'done4', 'date4', 'month4', 'name4', 'year4'
                                        , 'country5','product5', 'band5', 'sold5', 'price5', 'sale5', 'discount5', 'sales5', 'cogs5', 'profit5', 'done5', 'date5', 'month5', 'name5', 'year5'])

df_Input.set_index('segment', inplace=True)

result = df_Input.loc[Input]
print(result)

path = "sample.xlsx"
book = load_workbook(path)

writer = pd.ExcelWriter(path, engine='openpyxl')
writer.book = book
if 'Mastersheet' in book.sheetnames:
    ref = book['Mastersheet']
    book.remove(ref)

result.to_excel(writer, sheet_name='Mastersheet')

writer.save()
writer.close()
