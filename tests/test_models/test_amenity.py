import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
class TestCity(unittest.TestCase):
    """test for amenity"""
    def test_amenity_name(self):
        """test name amenity"""
        my_amenity1 = Amenity()
        my_amenity1.name = "pillows"
        