import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime

class TestUser(unittest.TestCase):
    """tests for user class"""
    
    def test_User(self):
        my_user1 = User()
        my_user1.first_name = "Harry"
        my_user1.last_name = "Jackson"
        my_user1.email = "hiproject1@mail.com"
        my_user1.password = "project"
        my_user1.save()
        self.assertEqual(my_user1, my_user1)