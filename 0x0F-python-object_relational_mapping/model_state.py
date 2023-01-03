#!/usr/bin/python3
""" Module documentation for State class definition
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ Declaration of the State class

    Attr:
        __tablename__ (str): Name of the table in the db
        id (int): Id of each row
        name (str): name of each row
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
