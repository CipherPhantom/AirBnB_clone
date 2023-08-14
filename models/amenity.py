#!/usr/bin/python3
"""
This module contains the class ``Amenity`` which inherits
from ``BaseModel``
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class defines attributes/methods for Amenity.

    Attributes:
        name(str):  Name of Amenity. Empty string initially
    """
    name = ''
