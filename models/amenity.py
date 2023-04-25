#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """ Defines Amenity class. """
    __tablename__ = 'amenities'
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

        place_amenities = relationship('Place', secondary=place_amenity,
                                       viewonly=False, backref='amenities')
    else:
        name = ""
