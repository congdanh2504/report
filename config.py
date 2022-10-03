import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
NAME = os.getenv("DB")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASS")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"