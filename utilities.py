class Utilities:
    
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
import smtplib, ssl, email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, reciver_email, subject, message, file_names=None):
    # Crea l'oggetto del messaggio
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = reciver_email
    msg['Subject'] = subject

    # Aggiunge il corpo del messaggio
    msg.attach(MIMEText(message, 'plain'))

    # Aggiunge gli allegati, se presenti
    if file_names:
        for fileName in file_names:
            with open(fileName, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{fileName}"')
            msg.attach(part)
            
    text = msg.as_string()        
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, reciver_email, text)

#     # Connette al server SMTP di Gmail
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(sender_email, sender_password)

#     # Invia il messaggio
#     server.send_message(msg)
#     server.quit()



    

# # Specifica gli allegati, se necessario
# attachments = [path_transfer]
# # Esempio di utilizzo
# sender_email = 'prova.test.camerana@gmail.com'
# sender_password = 'Ppbd01!!!'
# recipient_email = 'kpanik@gmail.com'
# subject = 'Curriculum Candidati'
# message = 'Questo è il corpo del messaggio.'
#     # Invia l'email
# send_email(sender_email, sender_password, recipient_email, subject, message, attachments)
# print('ok')

