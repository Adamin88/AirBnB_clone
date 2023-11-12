#!/usr/bin/python3
"""
BaseModel Module

This module defines the BaseModel class, which serves as the parent class
for all other classes used in the AirBnB clone project.
It handles the initialization, serialization, and deserialization of instances.

Classes:
- BaseModel: The base class for all objects in the AirBnB clone project.

Attributes:
- id (str): A unique identifier generated for each instance.
- created_at (datetime): The timestamp indicating the instance's creation time.
- updated_at (datetime): The timestamp indicating the instance's last update

Methods:
- __init__(self, *args, **kwargs): The constructor for BaseModel instances.
- __str__(self): Returns a string representation of the instance.
- save(self): Updates the instance's updated_at
attribute and saves the instance to a JSON file.
- to_dict(self): Returns a dictionary
representation of the instance for serialization.

Usage:
from models.base_model import BaseModel

# Instantiate BaseModel
base_model = BaseModel()

# Perform operations on the instance
base_model.save()
base_model_dict = base_model.to_dict()

"""
import uuid
from datetime import datetime
from models.engine.file_storage import storage


class BaseModel:
    """
    The BaseModel class defines all common attributes/methods
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel class. Initializes instance
        attributes based on provided
        keyword arguments or generates default values for id, created_at,
        and updated_at.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(
                        self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
            return
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance,
        including its class name, id, and attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance attributes into a dictionary representation
        with 'simple object type'.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
