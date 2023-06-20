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

    records = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id)
    if records is None:
        print("Nothing")
    else:
        for col in records:
            print(col.id, col.name, sep=': ')
