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
        if path == None:
            return True
        else:
            if not path.endswith("/"):
                path += "/"

        if excluded_paths == None:
            return True
        else:
            for excluded_path in excluded_paths:
                if path in excluded_path:
                    return False
        return True


    def authorization_header(self, request=None) -> str:
        """
        to return request which by default is None
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
        to return None for now
        """
        return None
