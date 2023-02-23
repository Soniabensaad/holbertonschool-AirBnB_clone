import unittest
from models.city import City
from models.base_model import BaseModel
class TestCity(unittest.TestCase):
    """tests for city class"""
    def test_city(self):
        """test for  city"""
        my_city1 = City()
        my_city1.name = "New York"
        my_city1.state_id = "9bf17966-b092-4996-bd33-26a5353cccb4"
        my_city1.save()
        self.assertEqual(str(my_city1), str(my_city1))
        

