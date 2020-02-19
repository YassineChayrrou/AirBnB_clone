#!/usr/bin/python3
"""
BaseModel that defines all common attributes/methods for other classes.
dev branch
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """Class constructor, creates a new instance
           of a class
           Args:
               *args (tuple): arguments of function
               **kwargs (dict): argument dictionary of function
           Public Attrib:
               id (str): id of an instance when it's created
               created_at (datetime):
               updated_at (datetime):
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints this format:
               [<class name>] (<self.id>) <self.__dict__>
        """
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute updated_at
           with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
           of __dict__ of the instance
        """
        # This doesn't work
        # I still don't know why
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        d = self.__dict__
        d['__class__'] = self.__class__.__name__
        return(d)
        """
        d = {}
        for key, value in self.__dict__.items():
            if key == 'created_at':
                d['created_at'] = self.created_at.isoformat()
            elif key == 'updated_at':
                d['updated_at'] = self.updated_at.isoformat()
            else:
                d[key] = value
        d['__class__'] = self.__class__.__name__
        return(d)
