import unittest
from models.state import State
from models.base_model import BaseModel
class TestState(unittest.TestCase):
    """tests for state class"""
    def test_state(self):
        """test for name state"""
        my_state1 = State()
        my_state1.name = "United State of America"
        my_state1.save()
        self.assertEqual(str(my_state1), str(my_state1))
    
    def test_state_attributes(self):
        """attributes"""
        self.assertIsInstance(State.name, str)
       
