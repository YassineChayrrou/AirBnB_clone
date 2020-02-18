#!/usr/bin/python3
"""
Storing first object
"""
import json
import os


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes
       JSON file to instances
    """

    def all(self):
        """returns the dictionary __objects
        """

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
           file (__file_path) exists)
        """
