import pandas as pd
import warnings
from datetime import date 


# APERTURA FILES
warnings.simplefilter(action="ignore", category=UserWarning)
xlsxFileHrr = pd.ExcelFile("C:\\Users\\amirk\\Desktop\\ACE10001I C-Lab HR\\ACE10001I C-Lab HR\\DB C-Lab (HRR).xlsx")
xlsxFileTrf = pd.ExcelFile("C:\\Users\\amirk\\Desktop\\ACE10001I C-Lab HR\\ACE10001I C-Lab HR\\DB C-Lab (Transfer).xlsx")
anagHrr = pd.read_excel(
    xlsxFileHrr,
    sheet_name="AnagSkill",
    header=0,
)
candHrr = pd.read_excel(
    xlsxFileHrr,
    sheet_name="Candidati",
    header=0,
)
anagTrf = pd.read_excel(
    xlsxFileTrf,
    sheet_name="AnagSkill",
    header=0,
)
candTrf = pd.read_excel(
    xlsxFileTrf,
    sheet_name="Candidati",
    header=0,
)

candHrrKeys = []

for index, row in anagTrf.iterrows():
    for key, val in row.items():
        if key not in candHrrKeys:
            candHrrKeys.append(key)
            
with pd.ExcelWriter('prova.xlsx') as writer:
    candHrr.to_excel(writer, index=False, sheet_name='Candidati')
    anagHrr.to_excel(writer, index=False, sheet_name='AnagSkill')