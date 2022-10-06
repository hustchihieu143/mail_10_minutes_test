from sqlalchemy import Table, Column
import sys
sys.path.insert(0,'/home/chihieu/project_web/test_poetry/config')
from db import meta
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

email_data = Table('emailData', meta,
            Column('id', Integer, primary_key=True),
            Column('receiver_id', Integer, nullable=False), 
            Column('sender', String, nullable=False),
            Column('content', String, nullable=False),
            Column('created_at', DateTime)
          )
