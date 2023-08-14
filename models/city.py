#!/usr/bin/python3
"""
This module contains the class ``City`` which inherits
from ``BaseModel``
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class defines attributes/methods for the City.

    Attributes:
        state_id(str):  It will be the State.id. Empty initially
        name(str):  Name of City. Empty string initially
    """
    state_id, name = ('', '')
