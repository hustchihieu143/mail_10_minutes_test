from fastapi import APIRouter
import sys
#sys.path.insert(0,'/home/chihieu/project_web/test_poetry/config')
#sys.path.insert(1,'/home/chihieu/project_web/test_poetry/models')
from config.db import conn
from models.index import email_data

email_data_router = APIRouter()

#test
@email_data_router.get("/get_data")
def read_data():
  return conn.execute(email_data.select()).fetchall()

#test
@email_data_router.post("/email_data")
def create_data(name:str):
    data = conn.execute(email_data.insert().values(
      receiver_id=1,
      sender="chihieusky@gmail.com",
      content="hello"
    ))
    return data.is_insert