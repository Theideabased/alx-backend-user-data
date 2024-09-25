#!/usr/bin/env python3
"""DB module
This will help us eto asses the db library and
and get the authenticated value out
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User
from user import Base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email, hashed_password):
        """ This will return user object """
        new_user = User(email=email, hashed_password=hashed_password)

        # Add the new user to the session
        self._session.add(new_user)
        
        # Commit the transaction
        self._session.commit()

        # Return the newly create user
        return new_user

    def find_user_by(self,**kwargs):
        """ This will take any argument from the table name
        then find the value of the first occurence of such 
        argument """
        valid_columns = [column.name for column in User.__table__.columns]

        for key in kwargs.keys():
            if key not in valid_columns:
                raise InvalidRequestError()

        try:
            user = self.__session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound()
            return user
        except NoResultFound:
            raise NoResultFound()



    def update_user(self, user_id: int, **kwargs):
        """ this will first user the find_user_by function to find the 
        first occurence then it will update that occurence to the new 
        value that is require """
        valid_columns = [column.name for column in User.__table__.columns]
        for key in kwargs.keys():
            if key not in valid_columns:
                raise ValueError
        if user_id == User.id:
            session.commit()
        else:
            return ValueError


