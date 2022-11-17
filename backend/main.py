from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import add_user, get_user, update_user, delete_user
from validate_email import validate_email
import phonenumbers
from dotenv import dotenv_values
from fastapi_login import LoginManager

config = dotenv_values(".env")

app = FastAPI()

login_manager = LoginManager(config["SECRET"], "/auth/login", use_cookie=True)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "hello why r u here"}

@app.get("/add_user")
async def add_user_endpoint(name, email, password, city, sports, age, phone):
    if not validate_email(email):
        return {"message": "Invalid Email"}
    elif sports == "":
        return {"message": "Enter at least 1 sport"}
    elif not phonenumbers.is_valid_number(phonenumbers.parse(phone, None)):
        return {"message": "Invalid Phone Number"}
    else:
        sports = sports.split(",")
        if add_user(name, email, password, city, sports, age, phone):
            return {"message": "Sign up successful!"}
        else:
            return {"message": "Unexpected Error, Try Again Later"}