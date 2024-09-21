#!/usr/bin/env python3
""" this is the class of the basic authentication this will contain
different function that will be used to enocode and decode using base64
the class have the function
extract_base64_authorization_header, decode_base64_authorization_header
extract_user_credentials and user_objects_from_credentials
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
import re
from typing import TypeVar


class BasicAuth(Auth):
    """ this authentication for basic authentication
    in flask this class will inherit from Auth
    and it will be the functions that will be
    used for Basic Auth of our project on flask
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ This function will extract the header of a
        request if it is has authentication and if
        the authentication is the correct one
        then it will return the value of the
        authentication
        """
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ This function will decode the header
        first check if it is in base64 then it
        will decode the base64 so that it can
        return the value of the decode result
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        s = base64_authorization_header
        if s is None or not isinstance(s, str):
            return None
        try:
            decoded_bytes = base64.b64decode(s)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except (base64.binascii.Error, ValueError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ This will extract the user credentials in the
        decoded value so that it can be used by the
        user instance when needed
        """

        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        dba_header = decoded_base64_authorization_header.split(":", 1)
        if len(dba_header) != 2:
            return None, None
        return dba_header[0], dba_header[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar(User):
        """ Class method to return a User object if the credentials are
        valid.
        this class will use the search function the is in the auth from
        the base.py to search the file after authentication
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None
        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ This will help us get the current user in the instance
        and then use it to work out things when necessary and
        this will futher get us the user instance
        """
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None
        extract = self.extract_base64_authorization_header(auth_header)
        if not extract:
            return None
        decode = self.decode_base64_authorization_header(extract)
        if not decode:
            return None
        extract_user = self.extract_user_credentials(decode)
        if extract_user:
            user_email, user_pwd = extract_user
            user_object = self.user_object_from_credentials(
                    user_email, user_pwd)
            return user_object
