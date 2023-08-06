#!/usr/bin/python3
"""doc"""
import sys
import unittest
from console import HBNBCommand


class test_console(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def setUp(self):
        '''setup for'''
        self.backup = sys.stdout

    def tearDown(self):
        """_summary_
        """
        sys.stdout = self.backup

    def create(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return HBNBCommand()

    def test_quit(self):
        """_summary_
        """
        console = self.create()
        self.assertTrue(console.onecmd("quit"))
