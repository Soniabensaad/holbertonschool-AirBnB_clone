#!/usr/bin/python3
"""city Class.
This module contains a class that inherits from the BaseModel class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string"""
    state_id = ""
    name = ""

    def __str__(self):
        return (f"[City] ({self.id}) {self.__dict__}")
