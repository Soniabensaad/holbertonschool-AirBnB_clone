#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Creates new instances of class.
        """
        pass
    def all(self):
        return  self.__objects
    def new(self, obj):
        obj_name = __class__.__name__
        obj_id = obj.id
        key = f"{obj_name}.{obj_id}"
        self.__objects[key] = obj

    def save(self):
        dictionnary = {}
        for key, value in self.__objects.items():
            dictionnary.update({key: value.to_dict()})
        json_f = json.dumps(dictionnary)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json_f)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                data = f.read()
                for key, value in data.items():
                    for key, value in data.items():
                        class_name = value['__class__']
                        del value['__class__']
                        obj = eval(class_name)(**value)
                        self.__objects[key] = obj
        except BaseException:
            pass

