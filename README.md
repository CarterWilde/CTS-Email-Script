# Prerequisites

Postgres SQL installed

Python 3 installed

Have a table with id, student_email and student_name

## Installing

Install python-dotenv
`pip install -U python-dotenv`

Install psycopg2
`pip install psycopg2`

## Starting

for csv
`py CTSEmailScript.py`

for db
`py CTSEmailScript.py -db`

### `.env` Example
```
CONTENT_FILE_PATH="email_content"
SENDER_EMAIL="carterjwilde@gmail.com"
EMAIL_SUBJECT="Greeting"
LOGIN_USER="<username>"
LOGIN_PASS="<password>"
DB_NAME="<db name>"
DB_USER="<db user>"
DB_PASSWORD="<db password>"
SQL_AMOUNT="10"
SQL_START_OFFSET="0"
SQL_TABLE="scheme.registration"
SMTP_PORT="587"
SMTP_ADDRESS="smtp.office365.com"
EMAILS_PATH="emails.csv"
```

### CONTENT_FILE Example
```
Hello {},
All the best!
```