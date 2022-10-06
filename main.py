from fastapi import FastAPI
import sys
sys.path.append('./')
from routes.index import emailRouter
from routes.index import emailDataRouter

app = FastAPI()

app.include_router(emailRouter)

app.include_router(emailDataRouter)
