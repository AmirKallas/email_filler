import openpyxl
import datetime

HRR_PATH = 'C:\\Users\\amirk\\Desktop\\filler_data\\DBC-Lab(HRR).xlsx'
TRANSFERT_PATH = 'C:\\Users\\amirk\\Desktop\\filler_data\\DBC-Lab(Transfer).xlsx'

hrrWorkbook = openpyxl.load_workbook(HRR_PATH, read_only=True, data_only=True)
candidatiHrr = hrrWorkbook['Candidati']

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
print(row_cells)

# lines_list = [row_cells for row_cells in range(0, len(row_cells)+1, 25)]

# lines_list = []
# for i in range(0, len(row_cells)+1):
    


# print(lines_list)

# print(row_cells)




