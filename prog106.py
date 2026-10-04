from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import create_engine
from prog104 import Employee

engine = create_engine('postgresql+psycopg2://postgres:Tory123@localhost:5432/lucy')


# with Session(engine) as session:
#     stmt = select(Employee)
#     data = session.scalars(stmt).all()

#     for d in data:
#         print(d.name)
#         print(d.department)
#         print(d.salary)

with Session(engine) as session:
    stmt = select(Employee).where(Employee.department == 'Finance')
    data = session.scalars(stmt).all()

    for d in data:
        print(d.name,d.department)
        


    






