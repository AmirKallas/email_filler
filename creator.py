import openpyxl
import datetime

HRR_PATH = 'C:\\Users\\amirk\\Desktop\\filler_data\\DBC-Lab(HRR).xlsx'
TRANSFERT_PATH = 'C:\\Users\\amirk\\Desktop\\filler_data\\DBC-Lab(Transfer).xlsx'

hrrWorkbook = openpyxl.load_workbook(HRR_PATH, read_only=True)

candidatiHrr = hrrWorkbook['Candidati']
cell = str(candidatiHrr.cell(row=2, column=21 ).value)
today  = str(datetime.date.today())
oggi = cell[0:10]

rows = candidatiHrr.max_row
cols = candidatiHrr.max_column

# print(type(today))
# print(type(cell))
# print(today)
# print(oggi)
# print(today == oggi)
# print(rows)
# print(cols)

for row_num in range(1, 5):
    dataCell = candidatiHrr.cell(row=row_num, column=21).value
    data = str(dataCell)[0:10]
    if data == today:
        print(dataCell)

# dataCell = str(candidatiHrr.cell(row=2, column=21).value)[0:10]
# print(dataCell)