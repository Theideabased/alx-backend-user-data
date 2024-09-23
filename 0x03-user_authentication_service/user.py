#!/usr/bin/env python3
""" This will create the necessary class for my authentication
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class User(Base):
    """ This is the user model for the dataset to authenticate
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
