import unittest
from models.review import Review
from models.base_model import BaseModel
class TestReview(unittest.TestCase):
    """tests for review class"""
    def test_review(self):
        """test for review attributes """
        my_review1 = Review()
        my_review1.place_id = "9bf17966-b092-4996-bd33-26a5353cccb4"
        my_review1.user_id = "af9b4cbd-2ce1-4e6e-8259-f578097dd15f"
        my_review1.text = "great place"
        my_review1.save()
        self.assertEqual(str(my_review1), str(my_review1))