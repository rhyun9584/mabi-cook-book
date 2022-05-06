import pandas as pd
from sqlalchemy import create_engine

table = pd.read_excel("./db_import/cook_list.xlsx", header=0, index_col=0)

engine = create_engine("mysql+pymysql://mabi:1234@127.0.0.1:3306/mabi_cook", encoding='utf-8')
table.to_sql(name="cook", con=engine, if_exists='append', index=False)