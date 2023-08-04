#!/usr/bin/python3
"""unit test"""

import unittest
from console import HBNBCommand


class test_Console(unittest.TestCase):

    def test_create(self):
        """ """
        return HBNBCommand()


if __name__ == '__main__':
    unittest.main()
