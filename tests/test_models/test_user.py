#!/usr/bin/python3
""" doc """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """ test user """

    def __init__(self, *args, **kwargs):
        """ test init """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test first name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ test email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ test pwd """
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == "__main__":
    unittest.main()
