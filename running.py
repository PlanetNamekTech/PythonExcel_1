import pandas as pd
from openpyxl.workbook import Workbook

#grab data from respective files
df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None)
df_txt = pd.read_csv('data.txt', delimiter='\t')

df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code']
#save the modified file as an excel file in this folder
df_csv.to_excel('modified.xlsx')

print(df_excel)