import unittest
from models.city import City
from models.base_model import BaseModel
class TestCity(unittest.TestCase):
    """tests for city class"""
    def test_city_id(self):
        """test id  city"""
        self.assertIsInstance(self.state_id, str)

    def test_city_name(self):
        """test name city"""
        self.assertIsInstance(self.name, str)

