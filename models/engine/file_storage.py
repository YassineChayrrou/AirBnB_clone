"""
Storing first object
"""
import json
import os


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes
       JSON file to instances
    """
    __file_path = storage.json
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return(FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[obj.__class__.__name__.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        with open(__file_path, 'w') as f:
            json.dump(obj)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
           file (__file_path) exists)
        """
        if os.path.isfile(__file_path):
            with open(__file_path, 'r') as f:
                load_json = json.load(f)
                return(load_json)
