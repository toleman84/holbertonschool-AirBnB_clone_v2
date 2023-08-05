#!/usr/bin/python3
""" doc """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class TestBasemodel(unittest.TestCase):
    """ test base model """

    def __init__(self, *args, **kwargs):
        """ test init """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ test setup """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ test default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ test kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ test kwargs int """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ test str """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ test to dict """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_id_float(self):
        """ test id float """
        new = self.value()
        self.assertNotEqual(type(new.id), float)

    def test_id_int(self):
        """ test id int """
        new = self.value()
        self.assertEqual(type(new.id), int)

    def test_id(self):
        """ test id """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ test created """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test updated """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == "__main__":
    unittest.main()
