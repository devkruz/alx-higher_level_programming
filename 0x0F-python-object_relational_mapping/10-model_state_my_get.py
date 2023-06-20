#!/usr/bin/python3
"""Print States Object"""
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

    records = session.query(State).filter(State.name == (argv[4], )).all()
    if records == []:
        print("Not found")
    else:
        for col in records:
            print(col.id)
