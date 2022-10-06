from sqlalchemy import Table, Column
import sys
sys.path.insert(0,'/home/chihieu/project_web/test_poetry/config')
from db import meta
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

email = Table('email', meta,
            Column('id', Integer, primary_key=True), 
            Column('name', String, unique=True, nullable=False),
            Column('created_at', DateTime)
          )
