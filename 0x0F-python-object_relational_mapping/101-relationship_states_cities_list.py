#!/usr/bin/python3
""" Script that runs queries using relationship in ORM
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
    query = session.query(State).outerjoin(City).order_by(State.id, City.id)
    for state in query.all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    # Close session
    session.close()
