#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from sqlalchemy.ext.declarative import declarative_base

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity',
                                 secondary=place_amenity, viewonly=False,
                                 back_populates='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """returns the list of Review"""
            rev_list = []
            for key, value in models.storage.all().items():
                if value.__class__.__name__ == 'Review' and \
                        value.place_id == self.id:
                    rev_list.append(value)
            return rev_list

        @property
        def amenities(self):
            """returns list of Amenity instances based on
            amenity_ids containing Amenity.id linked to Place """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """ append method for adding an Amenity.id
            to the attribute amenity_ids """
            if type(obj) == 'Amenity' and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
            else:
                pass
