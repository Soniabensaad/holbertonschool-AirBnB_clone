#!/usr/bin/python3
"""review Class.
This module contains a class that inherits from the BaseModel class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes:
      place_id: string - empty string: it will be the Place.id
      user_id: string - empty string: it will be the User.id
      text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
    def __str__(self):
        return (f"[Review] ({self.id}) {self.__dict__}")
