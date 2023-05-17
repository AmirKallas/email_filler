import pandas as pd
import warnings
from datetime import date 


# APERTURA FILES
warnings.simplefilter(action="ignore", category=UserWarning)
xlsFile = pd.ExcelFile("C:\\Users\\amirk\\Desktop\\ACE10001I C-Lab HR\\ACE10001I C-Lab HR\\DB C-Lab (HRR).xlsx")
anagHrr = pd.read_excel(
    xlsFile,
    sheet_name="AnagSkill",
    header=0,
)
candHrr = pd.read_excel(
    xlsFile,
    sheet_name="Candidati",
    header=0,
)
#print(candHrr) 
#print(candHrr.iloc[:5, :13])
# stato = candHrr[candHrr['Data invio CV al cliente'].str.contains('05-15-2023', na=False)]['Id candidato'].values
print(candHrr.head(1))
data = '2023-05-15 00:00:00'

#ISTANZA CONTENITORI DATI
idCand = []
candRows = []
anagRows = []

#LOOP PER ESTRAPOLARE RIGHE CANDIDTI E ID CANDIDATO DA USARE PER ANAGSKILL
for index, row in candHrr.iterrows():                 #cicla le righe nel Candidati sheet, compara la data
    if str(row['Data invio CV al cliente']) == data: #e riempie idCand di int corrispondenti all' id candidato
        candRows.append(row)
        #print(row['Nome'])
        id = row['Id candidato']
        if id not in idCand:
            idCand.append(id)
            
# print(type(idCand[0]))
# print(rows)


#LOOP PER ESTRAPOLARE RIGHE ANAGSKILL IN BASE A ID CANDIDATO (JOIN CON PROGR. INTERNO)
for index, row in anagHrr.iterrows():
    for num in idCand:
        if row['Progr Interno'] == num:
            anagRows.append(row)
            print(row['Nome'])
                       
    # print(row)
    
print(type(anagRows[0]))


            
        
         

    