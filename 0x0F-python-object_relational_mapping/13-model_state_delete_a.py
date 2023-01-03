#!/usr/bin/python3
""" Script that deletes all State objects with a name containing
    the letter a from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create Session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Code
    states_a = session.query(State).filter(State.name.like('%a%'))
    for instance in states_a:
        session.delete(instance)
    # Close session
    session.commit()
    session.close()
