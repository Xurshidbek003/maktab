from sqlalchemy import Column,Integer
from db import Base

class News(Base):

    __tablename__ = 'news'

    id = Column(Integer,primary_key=True,autoincrement=True)
    text = Column(Integer,nullable=False)