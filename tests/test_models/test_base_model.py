#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
class testBase_AirBnb(unittest.TestCase):

    def test_save(self):
        my_model = BaseModel()
        self.aassertEqual(my_model.save(), my_model.save())

    def test_base_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(
            (my_model_json), "{'my_number': 89, 'name': 'My First Model', 'updated_at': '2023-02-20 15:42:59.938285', 'id': '4a7e3d5c-d604-4dc2-89e1-733ae9b7079d', 'created_at': '2023-02-20 15:42:59.938256', '__class__': 'BaseModel'}")