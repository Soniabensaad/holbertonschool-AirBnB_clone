#!/usr/bin/python3
"""amenity Class.
This module contains a class that inherits from the BaseModel class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Public class attributes:
        name: string - empty string"""
    name = ""

    def __str__(self):
        return (f"[Amenity] ({self.id}) {self.__dict__}")
