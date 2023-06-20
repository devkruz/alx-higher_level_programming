#!/usr/bin/python3
"""List all States from Database"""
from model_city import Base, City
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for col in session.query(City).order_by(City.id):
        print(col.id, col.name, sep=': ')
