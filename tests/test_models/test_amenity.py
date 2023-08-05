#!/usr/bin/python3
""" doc """
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """ test amenity """

    def __init__(self, *args, **kwargs):
        """ test int """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test name """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
