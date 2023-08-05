#!/usr/bin/python3
"""unit test"""

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def test_create(self):
        """ test create """
        return HBNBCommand()


if __name__ == '__main__':
    unittest.main()
