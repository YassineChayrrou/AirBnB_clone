#!/bin/usr/python3
"""
User class that presents user related attributes
"""
from base_model import BaseModel
import json


class User(BaseModel):
    """
    User class inherits from BaseModel
    Public class attributes:
        email (str): empty string
        password (str): empty string
        first_name (str): empty string
        last_name (str): empty string
    """
    email = str
    password = str
    first_name = str
    last_name = str
