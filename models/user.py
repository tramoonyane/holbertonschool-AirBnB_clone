#!/usr/bin/python3
"""Module for User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
