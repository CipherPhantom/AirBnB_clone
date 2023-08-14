#!/usr/bin/python3
"""
This module contains the class ``User`` which inherits
from ``BaseModel``
"""
import uuid
import datetime
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines attributes/methods for the User.

    Attributes:
        email(str):     User email. Empty string initially
        password(str):  User Password. Empty string initially
        first_namestr): User First Name. Empty string initially
        last_name(str): User Last Name. Empty string initially
    """

    email, password, first_name, last_name = ('', '', '', '')
