#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata, Column('Place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False), Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', cascade='all, delete, delete-orphan', backref='place')
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)
    else:
        @property
        def reviews(self):
            """returns the list of Review"""
            rev_list = []
            for key, value in models.storage.all().items():
                if value.__class__.__name__ == 'Review' and value.place_id == self.id:
                    rev_list.append(value)
            return rev_list
        @property
        def amenities(self):

        
