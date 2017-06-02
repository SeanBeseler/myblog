from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
)

from .meta import Base



class Expense(Base):
    __tablename__ = 'expense'
    id = Column(Integer, primary_key=True)
    date = Column(Unicode)
    text = Column(Unicode)


