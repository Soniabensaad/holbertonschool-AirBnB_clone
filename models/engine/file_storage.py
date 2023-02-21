import json
import os
from models.base_model import BaseModel


class FileStorage:
   

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):

        dic = {}
        for key in self.__objects:
            dic[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w")as f:
            json.dump(dic, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                    class_name = value['__class__']
                    del value['__class__']
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except BaseException:
            pass
