#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel
class TestState(unittest.TestCase):
    """tests for place class"""
    def test_place_attributes(self):
        """test for place attributes """
        my_place1 = Place()
        my_place1.city_id = "080cce84-c574-4230-b82a-9acb74ad5e8c"
        my_place1.user_id = "af9b4cbd-2ce1-4e6e-8259-f578097dd15f"
        my_place1.description = "charming studio"
        my_place1.number_rooms = 2
        my_place1.number_bathrooms = 1
        my_place1.max_guest = 2
        my_place1.price_by_night = 65
        my_place1.latitude = 42.34
        my_place1.longitude = -71.12
        my_place1.amenity_ids = ["af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "9bf17966-b092-4996-bd33-26a5353cccb4"]
        my_place1.save()
        self.assertEqual(my_place1, my_place1)

    def test_place_attributes(self):
        """attributes"""
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.amenity_ids, list)