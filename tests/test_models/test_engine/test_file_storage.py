#!/usr/bin/python3
""" Defines a class TestFileStorage for FileStorage module. """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
FileStorage = FileStorage.FileStorage
classes = {"BaseModel": BaseModel}


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def test_all_filestorage(self):
        """Test that all  the FileStorage"""
        objects = storage.all()

        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        self.assertEqual(my_model, my_model)