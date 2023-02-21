#!/usr/bin/python3
import json
from models.base_model import BaseModel
class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return  self.__objects
    def new(self, obj):
        obj_name = __class__.__name__
        obj_id = obj.id
        key = f"{obj_name}.{obj_id}"
        self.__objects[key] = obj

    def save(self):
        dictionnary = {}
        for key, value in FileStorage.__objects.items():
            dictionnary[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionnary, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_loaded = json.load(f)

                new_obj_dict = {}
                for key, dict_obj in objects_loaded.items():
                    class_name = key.split(".")[0]
                    obj = eval(class_name)(**dict_obj)
                    new_obj_dict[key] = obj
                FileStorage.__objects = new_obj_dict
        except FileNotFoundError:
            pass
        
        

