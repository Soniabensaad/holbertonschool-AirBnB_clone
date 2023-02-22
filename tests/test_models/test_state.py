import unittest
from models.user import User
from models.base_model import BaseModel
class TestUser(unittest.TestCase):
    """tests for state class"""
    def test_state(self):
        """test for email user"""
        self.assertIsInstance(self.state.name, str)
