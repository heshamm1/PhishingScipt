import email
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from matplotlib.pyplot import text

with open ("password.txt", 'r') as file:
    password = file.read()

with open ("email.txt", 'r') as file:
    email = file.read()

with open ("text.txt", 'r') as file:
    text = file.read()

file = 'index.png'
image = open (file,'rb')
p=MIMEBase('application','octet-stream')
p.set_payload(image.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment ; filename = {file}')

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.ehlo()
server.login('spayteam6@gmail.com',password)

msg=MIMEMultipart()
msg['From'] = 'Spay Team'
msg['To'] = email 
msg['Subject'] = 'Lucky customer'
msg.attach(p)
msg.attach(MIMEText(text,'plain'))

message = msg.as_string()

server.sendmail('spayteam6',email.split(','),msg.as_string())

