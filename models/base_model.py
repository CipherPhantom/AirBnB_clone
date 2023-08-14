#!/usr/bin/python3
"""
This module contains the class ``BaseModel``
"""
import uuid
import datetime
from models import storage


class BaseModel:
    """
    This class defines all common attributes/methods for other classes.

    Attributes:
        id(str):  uuid assigned when an instance is created
        created_at: datetime - assign with the current
                    datetime when an instance is created
        updated_at: datetime - assign with the current
                    datetime when an instance is created
                    and update each time instance is changed.
    """

    def __init__(self, *args, **kwargs):
        if not bool(kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        setattr(self, k, datetime.datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """
        Returns a nicely formatted string
        representation for the BaseModel instance
        """
        return '[{}] ({}) {}'.format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        This function updates the public instance attribute
        ``updated_at`` with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        This function returns a dictionary containing
        all keys/values of __dict__ of the instance:
        """
        new_dict = {}

        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                new_dict[k] = v.isoformat()
            else:
                new_dict[k] = v
        new_dict['__class__'] = type(self).__name__
        return new_dict
