#!/usr/bin/python3
""" doc """
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """ test state """

    def __init__(self, *args, **kwargs):
        """ test init """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """ test name """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
