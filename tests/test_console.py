#!/usr/bin/python3
"""doc"""
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def test_precmd(self):
        """_summary_
        """
        pass

    def test_do_create(self):
        """_summary_
        """
        pass

    def test_do_show(self):
        """_summary_
        """
        pass

    def test_do_destroy(self):
        """_summary_
        """
        pass

    def test_do_all(self):
        """_summary_
        """
        pass

    def test_do_update(self):
        """_summary_
        """
        pass

    def test_emptyline(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        self.assertEqual(test_obj.emptyline(), None)

    def test_help(self):
        """_summary_
        """
        pass

    def test_quit(self):
        """_summary_
        """
        pass
