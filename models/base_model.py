#!/usr/bin/python3
"""
BaseModel class for AirBnB project.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class that defines common attributes/methods for other classes.
    It's the parent of other classes.
    """

    def __init__(self, *args, **kwargs):
        """Initialises a new instance or sets attributes based on kwargs"""
        format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            # Update attrs if provided in kwargs
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    # Convert str to datetime object
                    value = datetime.strptime(value, format)
                if key != '__class__':
                    # exclude __class__ from being set as an attr
                    setattr(self, key, value)
        else:
            # if no kwargs provided, use default values and store the new obj
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Returns BaseModel instance string representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates date and time of the instance and saves to file storage
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary of the instance attributes,
        with datetime objects converted to strings.
        """
        # make a copy to not modify the original
        dict_copy = self.__dict__.copy()
        # add class name
        dict_copy['__class__'] = self.__class__.__name__
        # convert datetime objects to str format
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy
