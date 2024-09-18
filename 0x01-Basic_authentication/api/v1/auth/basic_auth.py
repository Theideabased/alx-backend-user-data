#!/usr/bin/env python3
from api.v1.auth.auth import Auth
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
        elif type(base64_authorization_header) != str:
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
