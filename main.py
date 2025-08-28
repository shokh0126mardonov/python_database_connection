from psycopg2.pool import SimpleConnectionPool
from pprint import pprint
from config import PORT,PASSWORD,HOST,DBNAME,USER

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=5,
    host = HOST,
    port = PORT,
    password = PASSWORD,
    user = USER,
    dbname = DBNAME,
)
connection = pool.getconn()
cursor = connection.cursor()

cursor.execute(
    "DROP TABLE if exists test;"
)

cursor.execute(
    "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar(64));"
)

cursor.execute(
    "INSERT INTO test( num , data) VALUES (%s,%s)",(100,"salom")
)
cursor.execute(
    "INSERT INTO test( num , data) VALUES (%s,%s)",(123,"shohjahon")
)
cursor.execute(
    "INSERT INTO test( num , data) VALUES (%s,%s)",(432,"abdurauf")
)

cursor.execute('SELECT * FROM test;')
rows = cursor.fetchall()


connection.commit()
cursor.close()
connection.close()
pool.putconn(connection)