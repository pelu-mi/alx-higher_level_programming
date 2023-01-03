#!/usr/bin/python3
""" Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Create Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Base.metadata.create_all(engine)
    # Create Session
    Session = sessionmaker(bind=engine)
    session = Session()
    if session.query(State).first():
        instance = session.query(State).first()
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
