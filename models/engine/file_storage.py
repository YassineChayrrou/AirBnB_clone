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
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return(FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        s = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[s] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        d = {}
        for key, value in FileStorage.__objects.items():
            d[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
           file (__file_path) exists)
        """
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    for key, value in FileStorage.__objects.items():
                        FileStorage.__objects[key] = json.load(value)
        except:
            pass
