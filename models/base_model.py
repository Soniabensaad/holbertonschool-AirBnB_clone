#!/usr/bin/python3
import uuid
import datetime
"""Defines a class Base"""
class BaseModel:
    """ defines all common attributes/
    methods for other classes"""
    def __init__(self, name="", my_number=0):
            self.name = name
            self.my_number = my_number
            self.__class__ = BaseModel
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
        



    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = __class__.__name__
        new_dict["created_at"] = str(datetime.datetime.now())
        new_dict["updated_at"] = str(datetime.datetime.now())
        return new_dict


