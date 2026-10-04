from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import select

from prog104 import Employee

engine = create_engine('postgresql+psycopg2://postgres:Tory123@localhost:5432/lucy')

stmt = select(Employee).where(Employee.department=='HR')

with Session(engine) as session:
    data = session.scalars(stmt).all()
    for d in data:
        print(d.name,d.salary)

