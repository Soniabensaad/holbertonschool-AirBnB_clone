import unittest
from models.review import Review
from models.base_model import BaseModel
class TestReview(unittest.TestCase):
    """tests for review class"""
    def test_review_attributes(self):
        """test for review attributes """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)