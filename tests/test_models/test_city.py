#!/usr/bin/python3
""" doc """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ test city """

    def __init__(self, *args, **kwargs):
        """ test init """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test state id """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test name """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
