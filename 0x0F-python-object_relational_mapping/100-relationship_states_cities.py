#!/usr/bin/python3
""" Script that creates the State with the City in the database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    """ Code to run if file is not imported
    """
    # Create Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Create Session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Code
    c_state = State(name="California")
    c_city = City(name="San Francisco")
    c_state.cities.append(c_city)
    session.add(c_state)
    # Close session
    session.commit()
    session.close()
