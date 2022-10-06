from fastapi import FastAPI
import sys
from routes.index import email_router
from routes.index import email_data_router

app = FastAPI()

app.include_router(email_router)

app.include_router(email_data_router)
