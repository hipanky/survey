from sqlalchemy import create_engine,text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String,Integer,Numeric,Column



engine = create_engine('postgresql+psycopg2://postgres:Tory123@localhost:5432/lucy')

class Base(DeclarativeBase):
    pass

class Employee(Base):

    __tablename__ =  "employee"
    emp_id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    salary = Column(Integer)


Base.metadata.create_all(engine)




