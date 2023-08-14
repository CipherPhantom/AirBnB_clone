#!/usr/bin/python3
"""
This module contains the class ``FileStorage``
"""
import json


class FileStorage:
    """
    This class  serializes instances to a JSON file
    and deserializes JSON file to instances

    Attributes:
        __file_path(str): string - path to the JSON file (ex: file.json)
        __objects(dict): dictionary - empty but will store
                         all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This function simply returns the dictionary contained in the private
        class attribute __objects

        Returns:
            (dict): __objects
        """
        return (type(self).__objects)

    def new(self, obj):
        """
        This function sets a new object in the __objects
        dictionary with key <obj class name>.id

        Args:
            obj(`object`): Object to be added to dictionary
        """
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """
        This function serializes the dictionary contained in __objects,
        to the JSON file (path: __file_path)
        """
        all_dict = {k: v.to_dict() for k, v in
                    type(self).__objects.items()}
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            json_rep = json.dumps(all_dict)
            f.write(json_rep)

    def reload(self):
        """
        This function deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models import MODELS
        new_dict = {}

        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
            type(self).__objects = {k: MODELS[v['__class__']](**v)
                                    for k, v in new_dict.items()}
        except (FileNotFoundError, PermissionError,
                IOError, json.decoder.JSONDecodeError):
            return
