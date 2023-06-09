# Importo i moduli necessari
import pandas as pd
import datetime
import warnings
import os
import openpyxl

# Ignoro gli avvisi di errori nei file excel
warnings.simplefilter("ignore")

# Setto la variabile di ambiente User e setto il path dei file xlsx e pdf
userprofile = os.environ.get("userprofile")
#path_db = os.path.join("C:/Users", userprofile, "Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(HRR).xlsx")
# path_transfer = os.path.join("C:/Users", userprofile, "Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(Transfer).xlsx")
path_db = os.path.join("C:/Users/amirk/Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(HRR).xlsx")
path_transfer = os.path.join("C:/Users/amirk/Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(Transfer).xlsx")
#path_invio = os.path.join("C:/Users/amirk/Desktop/ACE10001_C-Lab_HR/prova(Transfer).xlsx")
path_invio = "C:/Users/amirk/Desktop/ACE10001_C-Lab_HR/prova(Transfer).xlsx"
def seleziona_e_copia_righe(path_db, path_dest):
    """Seleziona e copia le righe del foglio Candidati che contengono una data inserita dall'utente.

    Parametri:
    path_db (str): il path del file excel DB_C-Lab_(HRR)
    path_transfer (str): il path del file excel DB_C-Lab_(Transfer)

    """
    try:
        # Leggo il foglio Candidati
        candidati = pd.read_excel(path_db, sheet_name='Candidati')

        # Chiedo all'utente di inserire una data in formato dd/gg/yyyy e la converto in un oggetto
        user_date = input("Inserisci una data in formato dd/gg/yyyy: ")
        user_date = datetime.datetime.strptime(user_date, "%d/%m/%Y")

        # Formatto la data in una stringa con il formato yyyy-mm-dd
        user_date = user_date.strftime("%Y-%m-%d")

        # Seleziono le righe che contengono la data inserita dall'utente e le copio
        righe_selezionate = candidati[candidati.eq(user_date).any(axis=1)]
        copia_righe = candidati.loc[righe_selezionate.index]

        # Scrivo le righe selezionate nel file excel DB_C-Lab_(Transfer) nel foglio Candidati
        # with pd.ExcelWriter(path_dest, mode='w') as writer:
        #     copia_righe.to_excel(path_dest, index=False, sheet_name="Candidati", )

        # Leggo il file excel che contiene il foglio anagskill
        anagskill = pd.read_excel(path_db, sheet_name="AnagSkill")

        anagskill_df = pd.DataFrame(columns=anagskill.columns)
        # Create an empty list to store the rows
        rows = []

        # Loop through the rows of copia_righe
        for riga, row in copia_righe.iterrows():
            id = row['Id candidato']
            # Loop through the rows of anagskill
            for y, q in anagskill.iterrows():
                id2 = q['Progr Interno']
                if id2 == id:
                # Append the matching row to anagskill_df
                    anagskill_df = pd.concat([anagskill_df, q.to_frame().T])
                    print(anagskill_df)
                    cognome = q['Cognome']
                    nome = q['Nome']
                    # Incollo il Nome e Cognome
                    cognome_nome = cognome + '_' + nome
                    
                    # Creo una Lista di risultati trovato
                    nomi_curriculum = []
                    # Creo il Path del PDF da allegare
                    snippet = f"Desktop/ACE10001_C-Lab_HR/CV al Cliente/CV/cv_{cognome_nome}.pdf"
                    path_cv = os.path.join("C:/Users", userprofile, snippet) # type: ignore
                    print(path_cv)

                    # with pd.ExcelWriter(path_transfer, mode='a', if_sheet_exists="replace", engine='openpyxl') as writer:
                    #    anagskill_df.to_excel(writer, index=False, sheet_name='AnagSkill')


                    # with pd.ExcelWriter(path_transfer, engine='openpyxl', mode='a') as writer:
                    #     anagskill_df.to_excel(writer, index=False, sheet_name='AnagSkill')

        # with pd.ExcelWriter(path_dest, mode='a', engine= 'openpyxl', if_sheet_exists='replace') as writer:
        #     anagskill_df.to_excel(writer, index=False, sheet_name='AnagSkill')
            
        with pd.ExcelWriter(path_dest, mode='w') as writer:
            copia_righe.to_excel(writer, index=False, sheet_name="Candidati")
            anagskill_df.to_excel(writer, index=False, sheet_name='AnagSkill')           
        # Stampo le righe selezionate
        print(copia_righe)
        print('OOOOOOKKKK')
    
    # except ValueError:
    #    print("La data inserita non è valida. Riprova con un formato corretto.")
    
    except FileNotFoundError:
        print("Uno o entrambi i file excel non sono stati trovati. Controlla i path.")

# Chiamo la funzione seleziona_e_copia_righe con i path dei file xlsx
seleziona_e_copia_righe(path_db, path_invio)

import smtplib, ssl, email, yagmail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, recipient_email, subject, message, file_names=None):
    # Crea l'oggetto del messaggio
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Aggiunge il corpo del messaggio
    msg.attach(MIMEText(message, 'plain'))

    # Aggiunge gli allegati, se presenti
    if file_names:
        for fileName in file_names:
            with open(fileName, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            #encoders.encode_base64(part)  # Codifica l'allegato in base64
            #encoders.encode_7or8bit(part)
            part.add_header('Content-Disposition', 'attachment', filename=fileName)
            msg.attach(part)
            
    # text = msg.as_string()
    #print(text)
    print(msg)
    context = ssl.create_default_context()
 
    try:
        # yag = yagmail.SMTP(sender_email, sender_password, "smtp.gmail.com", 465)
        yag = yagmail.SMTP(sender_email, sender_password, "smtp.libero.it", 465)
        # yag.send(to=recipient_email, subject=subject, contents=text)
        yag.send(to=recipient_email, subject=subject, contents=msg)
        # smtp = smtplib.SMTP("smtp.gmail.com", 465)
        # # if isTls:
        # smtp.starttls()
        # smtp.login(sender_email, sender_password)
        # smtp.sendmail(sender_email, recipient_email, text)
        # smtp.quit()
    except Exception as e:
        print(e)


# Specifica gli allegati, se necessario
allegati = ["C:/Users/amirk/Desktop/ACE10001_C-Lab_HR/prova(Transfer).xlsx"]
# sender_email = 'prova.test.camerana@gmail.com'
# sender_password = 'PasswordNuova1'
sender_email = 'prova.camerana@libero.it'
sender_password = 'PasswordDifficile1!'
recipient_email = 'amir.kallas2cs@gmail.com'
subject = 'Curriculum Candidati'
message = 'Questo è il corpo del messaggio.'

send_email(sender_email, sender_password, recipient_email, subject, message, allegati)

print('ok')

