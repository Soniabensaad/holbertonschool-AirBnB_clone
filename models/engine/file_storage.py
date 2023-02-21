#!/usr/bin/python3
from models.base_model import BaseModel
import json
class FileStorage:
    """Defines the blueprint of saving and retrieving objects .
    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns every object created"""
        return FileStorage.__objects

    def new(self, obj):
        """Saves new objects with key class name.id in objects dictionary"""
        class_name = type(obj).__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        new_obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to objects"""
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
