from sqlalchemy import (
    create_engine,URL,text,Column,Table,String,MetaData,BOOLEAN,insert,Integer,select
    )
from config import PORT,HOST,DBNAME,PASSWORD,USER


url_object = URL.create(
    "postgresql+psycopg2",
    username=USER,
    password=PASSWORD, 
    host=HOST,
    port=PORT,
    database=DBNAME,
)

engine = create_engine(url_object)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id",Integer(),primary_key=True),
    Column("first_name",String(length=64),nullable=False),
    Column("last_name",String,nullable=True),
    Column("is_male",BOOLEAN)
)
metadata.create_all(engine)

with engine.connect() as conn:
    stmt = insert(users).values(first_name = 'Ali',last_name = 'Valiyev',is_male = True)
    conn.execute(stmt)
    conn.commit()
    
with engine.connect() as conn:
    stmt = select(users).where(users.c.id == 4)
    
    result = conn.execute(stmt)
    
    for row in result:
        print(row)