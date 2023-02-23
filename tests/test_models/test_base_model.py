#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
class testBase_AirBnb(unittest.TestCase):


    def test_base_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_model = "{'my_number': 89, 'name': 'My First Model', 'updated_at': '2023-02-20 14:24:01.871493', 'id': '853d2737-0bc7-4dbe-a403-b3934a3de25c', 'created_at': '2023-02-20 14:24:01.871499', '__class__': 'BaseModel'}")

        self.assertEqual(
            (my_model_json), "{'my_number': 89, 'name': 'My First Model', 'updated_at': '2023-02-20 14:24:01.871493', 'id': '853d2737-0bc7-4dbe-a403-b3934a3de25c', 'created_at': '2023-02-20 14:24:01.871499', '__class__': 'BaseModel'}")
    def test_assert(self):
        my_model = BaseModel()
        assert(my_model.save(), my_model.save())
        assert(my_model.id, my_model.id)
        assert(my_model.to_dict(), my_model.to_dict())