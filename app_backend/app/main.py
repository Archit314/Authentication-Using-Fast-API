from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# from config.database import init_db

app = FastAPI()

# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}