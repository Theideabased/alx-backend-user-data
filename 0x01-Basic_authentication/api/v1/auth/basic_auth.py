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
