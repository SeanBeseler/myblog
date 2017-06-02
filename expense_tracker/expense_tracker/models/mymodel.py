from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    DateTime
)

from .meta import Base



class Entry(Base):
    __tablename__ = 'entries'
    entry_id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    text = Column(Unicode)


