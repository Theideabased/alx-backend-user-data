#!/usr/bin/env/ python3
""" This is a function that will be used for auth """
import bcrypt


def _hash_password(password : str):
    """ this will use the bcyrpt to add salt and
    hash the password for security """
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return hash
