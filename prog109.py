from sqlalchemy.orm import DeclarativeBase,Session,mapped_column,Mapped
from sqlalchemy import Numeric,String,Integer,Column,create_engine


engine = create_engine('postgresql+psycopg2://postgres:Tory123@localhost:5432/my_db')

class Base(DeclarativeBase):
    pass

class tb1(Base):
    __tablename__ = "tb1"
    cid:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String)
    city:Mapped[str] = mapped_column(String)

with Session(engine) as session:
    data = session.query(tb1).all()

    for i in data:
        print(i.cid,i.name,i.city)


