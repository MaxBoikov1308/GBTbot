from sqlalchemy import Column, Integer, String
from data.dbapi import Base


class Users(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    __tablename__ = 'users'


class Requests(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=True)
    request = Column(String, nullable=True)
    __tablename__ = 'requests'