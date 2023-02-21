#!/usr/bin/python3
from models.base_model import BaseModel
import json
class FileStorage:
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
        for key, value in FileStorage.__objects.items():
            dictionnary.update({key: value.to_dict()})
        json_f = json.dumps(dictionnary)
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json_f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value["__class__"]
                    cls = globals()[cls_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

