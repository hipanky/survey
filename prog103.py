from sqlalchemy import create_engine,text

engine = create_engine('postgresql+psycopg2://postgres:Tory123@localhost:5432/postgres')


conn = engine.connect()
print(engine)
print(conn)

result = conn.execute(text('Select * from users'))

for row in result:
    print(row)

