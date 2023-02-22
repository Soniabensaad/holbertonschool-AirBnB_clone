#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State


class FileStorage:
   

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{obj_name}.{obj_id}"
        self.__objects[key] = obj

    def save(self):

        dictionnary = {}
        for key in self.__objects:
            dictionnary[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w")as f:
            json.dump(dictionnary, f)

    def reload(self):
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

