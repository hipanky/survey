import psycopg2
from sqlalchemy import create_engine

user='postgres'
password='Tory123'
host='127.0.0.1'
port=5432
database='postgres'

conn = psycopg2.connect(user=user,password=password,host=host,port=port,database=database)

if conn:
    print(f'conn exists')
else:
    print('No conn exists')

curr = conn.cursor()

print(curr)
query = '''
        Select * from sales2 where paymentmode = %s AND salesamount < %s
        '''
params = ("NetBanking",3000)

curr.execute(query,params)
result = curr.fetchall()

for row in result:
    print(row)


