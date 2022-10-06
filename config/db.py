from sqlalchemy import create_engine, MetaData

db_engine = create_engine("mysql+pymysql://test:1@localhost:3100/mail_10_minutes")
meta = MetaData()
conn = db_engine.connect()


