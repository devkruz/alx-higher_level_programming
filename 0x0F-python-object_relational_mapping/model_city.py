#!/usr/bin/python3
"""State Model"""
from sqlalchemy import MetaData, Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class City(Base):
    """State Modle Class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
