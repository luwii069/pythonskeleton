# db connection and environmental variables

from datetime import datetime, timedelta

from dotenv import load_dotenv

import os

load_dotenv()

conf = {
    "dbname": os.getenv("db_name"),
    "user": os.getenv("db_user"),
    "password": os.getenv("db_password"),
    "host": os.getenv("db_host"),
    "port": "5432",
}

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['dbname']}"
    JWT_SECRET_KEY = os.getenv("jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=20)
