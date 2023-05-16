import openpyxl
import datetime
import pandas as pd

HRR_PATH = 'C:\\Users\\amirk\\Desktop\\filler_data\\DBC-Lab(HRR).xlsx'
TRANSFERT_PATH = 'C:\\Users\\amirk\\Desktop\\filler_data\\DBC-Lab(Transfer).xlsx'

hrrWorkbook = openpyxl.load_workbook(HRR_PATH, read_only=True, data_only=True)
##transfertWorkbook = openpyxl.load_workbook(TRANSFERT_PATH, read_only=False, data_only=False)

candidatiHrr = hrrWorkbook['Candidati']
anagSkill = hrrWorkbook['AnagSkill']

# with open(HRR_PATH, 'r') as 

TODAY  = str(datetime.date.today())
stato = 'CV al Cliente'


rows = candidatiHrr.max_row
cols = candidatiHrr.max_column

row_cells = [] #lista di righe utili
for row_num in range(1, 5):
    if str(candidatiHrr.cell(row=row_num, column=21).value)[0:10] == TODAY and str(candidatiHrr.cell(row=row_num, column=20).value) == stato: #compara data odierna con data ria
        tempList = []
        for col_num in range(1, cols+1):
            value = candidatiHrr.cell(row=row_num, column=col_num).value
            tempList.append(str(value))
        row_cells.append(tempList)

# print(', '.join(row_cells))
# print(row_cells)

for riga in row_cells:
    idCandidato = int(riga[7])
    for row_num in range(1, 5):
        if anagSkill.cell(row=row_num, column=2).value == idCandidato:
            print('gino')
            tempList1 = []
            for col_num in range(1, cols+1):
                valore = candidatiHrr.cell(row=row_num, column=col_num).value
                tempList1.append(str(valore))
            print(tempList1)
            
            

        
    




