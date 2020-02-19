#!/usr/bin/python3
"""
Storing first object
"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes
       JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return(FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        s = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[s] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        d = {}
        for key, value in FileStorage.__objects.items():
            d[key] = value.to_dict()
        for key in d.keys():
            for k in key:
                if k == "__class__":
                    del(key[k])
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
           file (__file_path) exists)
        """
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    array = json.load(f)
                    for key, value in array.items():
                        tab = key.split('.')
                        my_instance = eval(tab[0])(**value)
                        self.new(my_instance)
        except:
            pass
