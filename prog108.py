#This work in case when table already created in postgres and want to read data

from sqlalchemy import create_engine, String, Integer, Numeric,Column

from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,Session

engine = create_engine('postgresql+psycopg2://postgres:Tory123@localhost:5432/my_db')

class Base(DeclarativeBase):
    pass

class C1(Base):
    __tablename__= "tb3"
    city:Mapped[str] = mapped_column(String,primary_key=True)
    rent:Mapped[int] = mapped_column(Numeric)

with Session(engine) as session:
    data = session.query(C1).all()

    for i in data:
        print(i.city,i.rent)







