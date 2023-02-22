import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime

class TestUser(unittest.TestCase):
    """tests for user class"""
    def test_email_user(self):
        """test for email user"""
        self.assertIsInstance(self.user.email, str)

    def test_password_user(self):
        """test for password user"""
        self.assertIsInstance(self.user.password, str)
    
    def test_first_name_user(self):
        """test for first_name user"""
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_user(self):
        """test for last_name user"""
        self.assertIsInstance(self.user.last_name, str)