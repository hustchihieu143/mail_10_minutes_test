from fastapi import APIRouter
import sys
sys.path.insert(0,'/home/chihieu/project_web/test_poetry/config')
sys.path.insert(1,'/home/chihieu/project_web/test_poetry/models')
from db import conn
from index import emailData

emailDataRouter = APIRouter()

#test
@emailDataRouter.get("/get_data")
async def read_data():
  return conn.execute(emailData.select()).fetchall()

#test
@emailDataRouter.post("/email_data")
async def create_data(name:str):
    data = conn.execute(emailData.insert().values(
      receiver_id=1,
      sender="chihieusky@gmail.com",
      content="hello"
    ))
    return data.is_insert