#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the database

"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like("%a%")).all()

    # Delete them
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
