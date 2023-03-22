#!/usr/bin/python3
""" This module defines a class to manage database storage for hbnb clone. """
from sqlalchemy import create_engine, Metadata
from sqlalchemy.orm import Session
from models.base_model import Base
import os


class DBStorage():
    """ Database storage class. """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize attributes. """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = 'localhost'
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://
                                      {user}:{pwd}@{host}
                                      /{db}', pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of models currently in database storage. """

        self.__session = Session(self.__engine)
        if cls is None:
            all_objs = self.__session.query('User', 'State', 'City'
                                     'Amenity', 'Place', 'Review').all()
            all_dict = {}
            for obj in all_objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                all_dict[key] = obj
            return (all_dict)
        else:
            cls_objs = self.__session.query(cls).all()
            cls_dict = {}
            for obj in all_objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                cls_dict[key] = obj
            return (cls_dict)

    def new(self, obj):
        """ Add the object to the current database session. """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session. """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session. """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database. """
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
