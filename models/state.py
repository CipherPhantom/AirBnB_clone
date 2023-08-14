#!/usr/bin/python3
"""
This module contains the class ``State`` which inherits
from ``BaseModel``
"""
from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class defines attributes/methods for the State.

    Attributes:
        name(str): Name of state.
    """

    name = ''
