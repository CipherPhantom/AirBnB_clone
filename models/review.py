#!/usr/bin/python3
"""
This module contains the class ``Review`` which inherits
from ``BaseModel``
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines attributes/methods for the Review.

    Attributes:
        place_id(string): empty string - it will be the Place.id
        user_id(str): empty string - it will be the User.id
        text(str): empty string
    """

    place_id, user_id, text = ('', '', '')
