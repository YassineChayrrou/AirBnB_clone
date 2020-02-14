"""
BaseModel that defines all common attributes/methods for other classes.
"""
import uuid
import datetime

class BaseModel:
    """BaseModel class
    """

    def __init__(self):
        """Class constructor, creates a new instance
           of a class
           Public Attrib:
               id (str): id of an instance when it's created
               created_at (datetime):
               updated_at (datetime):
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Prints this format:
               [<class name>] (<self.id>) <self.__dict__>
        """
        return("[{}] ({}) <{}>".format(self.__class__.__name__,
                                       self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute updated_at
           with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
           of __dict__ of the instance
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        d = self.__dict__
        d['__class__'] = self.__class__.__name__
        return(d)