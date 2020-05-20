import smtplib
import os
import psycopg2

from email.message import EmailMessage
from dotenv import load_dotenv

def GetContent(*arg):
  fp = os.getenv('CONTENT_FILE_PATH')
  cont = ''
  with open(fp, 'r') as file:
    for line in file.readlines():
      cont += line
    cont = cont.format(*arg)
    return cont

def ServerSetup(auth_user: str, auth_pass: str):
  s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  s.ehlo()
  s.login(auth_user, auth_pass)
  return s

def SendEmail(server: smtplib.SMTP_SSL, from_adder: str, to_adder: str, sub:str, content: str, auth_user: str, auth_pass: str):
  try:
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = sub
    msg['From'] = from_adder
    msg['To'] = to_adder
    server.send_message(msg)
  except smtplib.SMTPAuthenticationError:
    print('ERROR: Could not log you in.')
  except smtplib.SMTPSenderRefused:
    print('ERROR: Server Refused!')

def GetToAddressesAndNames():
  name = os.getenv('DB_NAME')
  usr = os.getenv('DB_USER')
  passw = os.getenv('DB_PASSWORD')
  con = psycopg2.connect(dbname=name, user=usr, password=passw)
  cursor = con.cursor()
  amount = os.getenv('SQL_AMOUNT')
  offset = os.getenv('SQL_START_OFFSET')
  table = os.getenv('SQL_TABLE')
  cursor.execute(f'SELECT student_email, student_name FROM {table} WHERE {table}.id > {offset} LIMIT {amount}')
  return cursor.fetchall()

load_dotenv(verbose=True)

user = os.getenv('LOGIN_USER')
passw = os.getenv('LOGIN_PASS')
from_add = os.getenv('SENDER_EMAIL')
sub = os.getenv('EMAIL_SUBJECT')

ser = ServerSetup(user, passw)

to_addresses_and_names = [
  ('carterjwilde@gmail.com', 'Carter Wilde')
]

to_addresses_and_names = GetToAddressesAndNames()

print(f"Emaling:")
for address in to_addresses_and_names:
  print(address)
choice = input('Are you sure! Y/N: ')
if(choice == 'Y'):
  for to_add_and_name in to_addresses_and_names:
    to_add = to_add_and_name[0]
    to_name = to_add_and_name[1]
    cont = GetContent(to_name)
    SendEmail(ser, from_add, to_add, sub, cont, user, passw)