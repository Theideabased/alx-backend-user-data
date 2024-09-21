#!/usr/bin/env python3
"""
creating an authentication class
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """
    This class will create a simple
    authentication for my apis
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        to return False for path and excluded_paths
        """
        if path is None or path == "":
            return True
        if not path.endswith("/"):
            path += "/"
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        else:
            for excluded_path in excluded_paths:
                if not excluded_path.endswith("/"):
                    excluded_path += "/"
                if path == excluded_path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        to return request which by default is None
        how ever if the authorization is avaliable we
        will return the authorization value
        """
        if request is None:
            return None
        else:
            response = request.headers
            if 'Authorization' not in response:
                return None
            else:
                name = response.get('Authorization')
        return name

    def current_user(self, request=None) -> TypeVar('User'):
        """
        to return None for now
        """
        return None
