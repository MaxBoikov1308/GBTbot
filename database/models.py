from sqlalchemy import (
    Column, Integer, String,
    Date, Text,
    ForeignKey, UniqueConstraint, 
    )
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    user_id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    date_added = Column(Date, nullable=False)
    __tablename__ = 'users'
