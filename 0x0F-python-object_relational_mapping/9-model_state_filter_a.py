#!/usr/bin/python3
""" Script that prints the State objects from the database hbtn_0e_6_usa
    containing the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Create Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create Session
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.like('%a%')).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
