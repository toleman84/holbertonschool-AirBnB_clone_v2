#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':

        cities = relationship('City', cascade='all, delete, delete-orphan',
                              backref='state')

    else:
        @property
        def cities(self):
            """ returns the list of City instances with
            state_id equals to the current State.id """
            cities_list = []

            for key, value in models.storage.all().items():
                if value.__class__.__name__ == 'City':
                    if value.state_id == self.id:
                        cities_list.append(value)
            return cities_list

        name = ''
