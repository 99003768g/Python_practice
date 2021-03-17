import pandas as pd
from openpyxl import load_workbook
def merge_sheet():
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

    df_Input = pd.DataFrame(file6,
                            columns=['segment', 'country2', 'product2', 'band2', 'sold2', 'price2', 'sale2', 'discount2',
                                     'sales2', 'cogs', 'profit2', 'done2', 'date2', 'month2', 'name2', 'year2'])

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
