#!/usr/bin/env python3
""" This is a function that will be used for auth """
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
user = User()


def _hash_password(password: str):
    """ this will use the bcyrpt to add salt and
    hash the password for security """
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return hash


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str):
        """ this will find if a user is already registered
        and if it is not registered it will hash the password and
        store it in the database"""
        try:
            x = self._db.find_user_by(email=email)
            raise ValueError(f"User {x.email} already exists")
        except NoResultFound:
            hash_pass = _hash_password(password)
            self._db.add_user(email, hash_pass)
            return user
