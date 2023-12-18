#!/usr/bin/python3
"""This script is doing something"""

from sqlalchemy import Column, engine, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """A class representing a state in the US."""
    __tablename__ = "states"

    name = Column(String(128), nullable=True)
    id = Column(Integer, primary_key=True)
