from fastapi import APIRouter
import random
import string
from datetime import datetime
import requests

#mail
import smtplib
from socket import gaierror
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

#config mailtrap
port = os.environ.get("PORT")
smtp_server = os.environ.get("SMTP_SERVER")
login = os.environ.get("LOGIN")
password = os.environ.get("PASSWORD")

import sys
sys.path.insert(0,'/home/chihieu/project_web/test_poetry/config')
sys.path.insert(1,'/home/chihieu/project_web/test_poetry/models')

from db import conn
from index import email
from index import email_data

email_router = APIRouter()


# send email from this email to that email
@email_router.post("/send-email")
def simple_send(sender: str, receiver: str, message: str):
  content = f"""\
        Subject: Hi Mailtrap
        To: {receiver}
        From: {sender}
        {message}."""

  try:
    #send your message with credentials specified above
    with smtplib.SMTP(smtp_server, port) as server:
        print(dirname(__file__))
        print(login)
        server.login(login, password)
        print("login successful")
        server.sendmail(sender, receiver, content)
        user = conn.execute(email.select().where(email.c.name == receiver)).fetchone()
        print('Sent')
        return conn.execute(email_data.insert().values(
          receiver_id=user.id,
          sender=sender,
          content=message,
        ))
        
    # tell the script to report if your message was sent or which errors need to be fixed 
   
  except (gaierror, ConnectionRefusedError):
    print('Failed to connect to the server. Bad connection settings?')
  except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
  except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))


# get all email in system
@email_router.get("/")
def read_data():
  print(os.path)
  return conn.execute(email.select()).fetchall()


# get inbox of email
@email_router.get("/inbox")
def get_inbox(name: str):
  user = conn.execute(email.select().where(email.c.name == name)).fetchone()
  result = datetime.utcnow().timestamp() - user.created_at.timestamp()
  
  
  if(user and result <= 10*60):
    return conn.execute(email_data.select().where(email_data.c.receiver_id == user.id)).fetchall()

# random email func
def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

# random email and save to database
@email_router.post("/")
def random_email_func():
    email_rand = random_char(8)+"@gmail.com"
    data = conn.execute(email.insert().values(
      name=email_rand
    ))
    return data.is_insert


