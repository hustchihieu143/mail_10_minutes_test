from sqlalchemy import create_engine, MetaData
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

db_config = port = os.environ.get("MYSQL_DATABASE_URL")

db_engine = create_engine(db_config)
meta = MetaData()
conn = db_engine.connect()


