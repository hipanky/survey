from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from prog104 import Employee
engine = create_engine('postgresql+psycopg2://postgres:Tory123@localhost:5432/lucy')

# with Session(engine) as session:
#     employee = Employee(
#         name="Rahul",
#         department="IT",
#         salary=50000
#     )
    
#     session.add(employee)
#     session.commit()

e1 = Employee(
        name="Rahul",
        department="IT",
        salary=50000
    )

e2 = Employee(
        name="Amit",
        department="HR",
        salary=45000
    )

e3 = Employee(
        name="Priya",
        department="Finance",
        salary=60000
    )
employees =[e1,e2,e3]

for employee in employees:
    with Session(engine) as session:
        session.add(employee)
        session.commit()



    





