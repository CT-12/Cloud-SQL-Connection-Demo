from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=".env")
db_host = os.getenv(key="DB_HOST") # IP address
db_user = os.getenv(key="DB_USER")
db_password = os.getenv(key="DB_PASSWORD")
db_name = os.getenv(key="DB_NAME")

DATABASE_URI = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
