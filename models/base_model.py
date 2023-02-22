
import uuid
from datetime import datetime
import models 
time_format = "%Y-%m-%dT%H:%M:%S.%f"
"""Defines a class Base"""
class BaseModel:
    """ defines all common attributes/
    methods for other classes"""
    def __init__(self, *args, **kwargs):
            if kwargs:
                 for key, value in kwargs.items():
                      if key != __class__:
                           if key == "created_at" or key == "updated_at":
                                self.__dict__[key] = datetime.strptime(value, time_format)
                           else:
                                self.__dict__[key] = value
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = self.created_at
                models.storage.new(self)



    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = __class__.__name__
        new_dict["created_at"] = self.created_at.strftime(time_format)
        new_dict["updated_at"] = self.updated_at.strftime(time_format)
        return new_dict


