# import openpyxl
import pandas as pd
# To read the various excel files
def read_excel_input():
    excel_file = pd.ExcelFile('sample.xlsx')
    pass


# To enter the keywords to be searched in excel sheets
def input_keywords():
    pass


# To search for keywords in read excel sheets
def search_keywords():
    pass


# To write found values into the mastersheet
def write_mastersheet():
    pass
    # if 'Mastersheet' in book.sheetnames:
    #     ref = book['Mastersheet']
    #     book.remove(ref)
    #
    # result.to_excel(writer, sheet_name='Mastersheet')
    #
    # writer.save()
    # writer.close()
