import os
from dotenv import load_dotenv


load_dotenv()

db = {
    'user': os.environ.get("DB_USER"),
    'password': os.environ.get("DB_PASSWORD"),
    'host': os.environ.get("DB_HOST"),
    'port': os.environ.get("DB_PORT"),
    'database': os.environ.get("DB_DATABASE"),
}
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db['user']}:{db['password']}@"\
                          f"{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(32)

# 이메일 전송을 위한 설정
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = os.environ.get("MAIL_USERNAME"),
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD"),
MAIL_USE_TLS = True
MAIL_USE_SSL = False
