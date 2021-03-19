import pandas as pd
from matplotlib import pyplot as pt

excel_file = pd.ExcelFile('book.xlsx')
something = input("ENTER SOMETHING: ")
PS = 99003768
NAME = "Undrajavarapu Vijay"
EMAIL = "undrajavarapu.vijay@ltts.com"

if "something " == PS:
    df = pd.DataFrame()

    for i in excel_file.sheet_names:
        df1 = pd.read_excel(excel_file, i)
        # check for input
        df1.set_index('PS_Number', inplace=True)

        result = df1.loc[input]
        print(result)

elif "something " == NAME:
    df = pd.DataFrame()

    for i in excel_file.sheet_names:
        df1 = pd.read_excel(excel_file, i)

        # check for input
        df1.set_index('Name', inplace=True)

        result = df1.loc[input]
        print(result)

elif "something " == EMAIL:
    df = pd.DataFrame()

    for i in excel_file.sheet_names:
        df1 = pd.read_excel(excel_file, i)

        # check for input
        df1.set_index('Email_Address', inplace=True)

        result = df1.loc[input]
        print(result)
df = pd.DataFrame({'PS_Number': ['A', 'B', 'C'], 'Team_No_1': [10, 30, 20]})
ax = df.plot.bar(x='PS_Number', y='Team_No_1', rot=0)
# pt.show()
