#!/usr/bin/python3
"""State Class.
This module contains a class that inherits from the BaseModel class."""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State (models/state.py):
       Public class attributes:
           name: string - empty string
    """
    name = ""
