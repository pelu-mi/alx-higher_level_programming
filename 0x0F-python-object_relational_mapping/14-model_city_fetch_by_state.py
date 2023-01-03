#!/usr/bin/python3
""" Script that prints all City objects from the database
"""

import sys
from model_state import Base, State
from model_city import City
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
    query = session.query(State, City).join(City).order_by(City.id)
    for s, c in query.all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    # Close session
    session.commit()
    session.close()
