#!/usr/bin/python3
"""new class to store data"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class FileStorage:
    """ serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{obj_name}.{obj_id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dictionnary = {}
        for key in self.__objects:
            dictionnary[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w")as f:
            json.dump(dictionnary, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for key, value in data.items():
                    class_name = value['__class__']
                    del value['__class__']
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except BaseException:
            pass
