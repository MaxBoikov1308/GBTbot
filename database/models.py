from sqlalchemy import (
    Column, Integer, String,
    Date, Text,
    ForeignKey, UniqueConstraint, 
    )
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Users(Base):
    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    username = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    __tablename__ = 'users'


class Request(Base):
    request_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    request = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    __tablename__ = 'request'
