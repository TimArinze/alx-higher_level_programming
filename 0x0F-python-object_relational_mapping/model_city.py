#!/usr/bin/python3
"""
model_city class
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """City class"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
