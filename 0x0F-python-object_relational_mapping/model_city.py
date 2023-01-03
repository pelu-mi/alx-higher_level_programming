#!/usr/bin/python3
""" Module documentation for City class definition
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ Declaration of the City class

    Attr:
        __tablename__ (str): Name of the table in the db
        id (int): Id of each row
        name (str): name of each row
        state_id (int): Foreign key on State.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
