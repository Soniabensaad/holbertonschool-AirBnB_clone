import unittest
from models.state import State
from models.base_model import BaseModel
class TestState(unittest.TestCase):
    """tests for state class"""
    def test_state(self):
        """test for name state"""
        self.assertIsInstance(self.state.name, str)
