#!/usr/bin/env python3
from api.v1.auth.auth import Auth
from models.user import User
import base64
import re
from typing import TypeVar
"""
this is the class of the
basic authentication
"""


class BasicAuth(Auth):
    """
    this authentication for basic authentication 
    in flask
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        elif type(authorization_header) != str:
            return None
        elif authorization_header.startswith('Basic ') != True:
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
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


    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):

        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        dba_header = decoded_base64_authorization_header.split(":", 1)
        if len(dba_header) != 2:
            return None,None
            
        return dba_header[0], dba_header[1]

    

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar(User):
        """ Class method to return a User object if the credentials are valid. """
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
            user_object = self.user_object_from_credentials(user_email, user_pwd)
            return user_object
