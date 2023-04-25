#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship('City', cascade='all, delete',
                              backref='state')

    else:
        name = ""

        @property
        def cities(self):
            """ Getter for cities attribute. """
            city_objs = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_objs.append(city)
            return city_objs
