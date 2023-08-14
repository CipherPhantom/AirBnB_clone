#!/usr/bin/python3
"""
This module contains the class ``Place`` which inherits
from ``BaseModel``
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This class defines attributes/methods for the Place.

    Attributes:
        city_id(str):       empty string - it will be the City.id
        user_id(str):       empty string - it will be the User.id
        name(str):          empty string
        description(str):   empty string
        number_rooms(int):  0
        number_bathrooms(int): 0
        max_guest(int):     0
        price_by_night(int): 0
        latitude(float):    0.0
        longitude(float):   0.0
        amenity_ids(list):  empty list of string -
                            it will be the list of Amenity.id.
    """

    city_id, user_id, name, description = ('', '', '', '')
    number_rooms, number_bathrooms, max_guest = (0, 0, 0)
    price_by_night, latitude, longitude, amenity_ids = (0, 0.0, 0.0, [])
