#!/usr/bin/python3
"""doc"""
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def test_precmd(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        test_cmd = "User.all()"
        new_cmd = test_obj.precmd(test_cmd)
        self.assertEqual(new_cmd, "User.all()")

    def test_do_create(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        test_cmd = "create User name=John Doe email=johndoe@example.com"
        test_obj.do_create(test_cmd)
        user = self.storage.all("User")["User.1"]
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "johndoe@example.com")

    def test_do_show(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        test_cmd = "show User 1"
        test_obj.do_show(test_cmd)
        user = self.storage.all("User")["User.1"]
        self.assertEqual(user, test_obj.last_printed)

    def test_do_destroy(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        test_cmd = "create User name=John Doe email=johndoe@example.com"
        test_obj.do_create(test_cmd)
        test_cmd = "destroy User 1"
        test_obj.do_destroy(test_cmd)
        user = self.storage.all("User")["User.1"]
        self.assertIsNone(user)

    def test_do_all(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        test_cmd = "create User name=John Doe email=johndoe@example.com"
        test_obj.do_create(test_cmd)
        test_cmd = "all User"
        test_obj.do_all(test_cmd)
        users = test_obj.last_printed
        self.assertIn("User.1", users)
        self.assertIn("name: John Doe", users)
        self.assertIn("email: johndoe@example.com", users)

    def test_do_update(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        test_cmd = "create User name=John Doe email=johndoe@example.com"
        test_obj.do_create(test_cmd)
        test_cmd = "update User 1 name=Jane Doe email=janedoe@example.com"
        test_obj.do_update(test_cmd)
        user = self.storage.all("User")["User.1"]
        self.assertEqual(user.name, "Jane Doe")
        self.assertEqual(user.email, "janedoe@example.com")

    def test_emptyline(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        self.assertEqual(test_obj.emptyline(), None)

    def test_help(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        test_cmd = "help"
        test_obj.do_help(test_cmd)
        self.assertIn("create", test_obj.last_printed)

    def test_quit(self):
        """_summary_
        """
        test_obj = HBNBCommand()
        test_cmd = "quit"
        test_obj.do_quit(test_cmd)
        self.assertEqual(test_obj.last_printed, "Exiting program...")
