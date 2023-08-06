#!/usr/bin/python3
"""doc"""
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def test_emptyline(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        self.assertEqual(test_obj.emptyline(), None)
