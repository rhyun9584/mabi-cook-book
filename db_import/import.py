import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

db = {
    'user': os.environ.get("DB_USER"),
    'password': os.environ.get("DB_PASSWORD"),
    'host': os.environ.get("DB_HOST"),
    'port': os.environ.get("DB_PORT"),
    'database': os.environ.get("DB_DATABASE"),
}

table = pd.read_excel("./db_import/cook_list.xlsx", header=0, index_col=0)

engine = create_engine(f"mysql+pymysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}", \
                       encoding='utf-8')
table.to_sql(name="cook", con=engine, if_exists='append', index=False)