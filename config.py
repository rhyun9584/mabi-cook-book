import os


db = {
    'user': 'mabi',
    'password': '1234',
    'host': 'localhost',
    'port': 3306,
    'database': 'mabi_cook',
}
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db['user']}:{db['password']}@"\
                          f"{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(32)
