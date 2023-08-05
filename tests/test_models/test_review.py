#!/usr/bin/python3
""" doc """
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """ test review """

    def __init__(self, *args, **kwargs):
        """ test init """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test place """
        new = self.value()
        self.assertNotEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test user """
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_text(self):
        """ test text """
        new = self.value()
        self.assertNotEqual(type(new.text), str)


if __name__ == "__main__":
    unittest.main()
