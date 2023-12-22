#!/usr/bin/python3
"""This script is doing something"""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base

class City(Base):
    """A class representing a city in the US."""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id', ondelete="CASCADE"), nullable=False)
