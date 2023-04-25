#!/usr/bin/python3
""" This module defines a class to manage database storage for hbnb clone. """
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
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
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True)
        self.__session = Session(self.__engine)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of models currently in database storage. """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.amenity import Amenity

        if cls is None:
            classes = [User, State, City, Place, Review, Amenity]
        else:
            classes = [cls]

        obj_dict = {}
        for c in classes:
            objs = self.__session.query(c).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dict[key] = obj

        return obj_dict

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
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """ Calls the remove method. """
        self.__session.close()
