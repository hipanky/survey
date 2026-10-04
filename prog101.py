import psycopg2
from sqlalchemy import create_engine

user='postgres'
password='Tory123'
host='127.0.0.1'
port=5432
database='postgres'

def get_conn():
    conn = psycopg2.connect(
                            user=user,
                            password=password,
                            host=host,
                            port=port,
                            database=database)
    return conn

def fetch_date():
    query = 'Select * from bookings'
    conn=get_conn()
    if conn:
        curr = conn.cursor()
        result = curr.query(query)
        for i in result:
            print(i)

    else:
        print('conn does not exist')


fetch_date()