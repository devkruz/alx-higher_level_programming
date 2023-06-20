#!/usr/bin/python3
"""List all States from Database"""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    records = session.query(State).order_by(State.id).all()[0]
    if records is None:
        print("Nothing")
    else:
        print(records.name)
