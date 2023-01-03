#!/usr/bin/python3
""" Script that changes the name of a State object from the database
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
    state_2 = session.query(State).filter(State.id == 2).first()
    state_2.name = "New Mexico"
    # Close session
    session.commit()
    session.close()
