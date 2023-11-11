#!/usr/bin/python3

import unittest
import sys
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch
from models import storage

class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up a clean testing environment."""
        self.console = HBNBCommand()
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Clean up resources after testing."""
        sys.stdout = sys.__stdout__

    @classmethod
    def tearDownClass(cls):
        """Clean up storage after all tests."""
        storage.reload()

    def test_quit(self):
        """Test the quit command."""
        with patch('builtins.input', return_value="quit"):
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF (Ctrl + D) command."""
        with patch('builtins.input', side_effect=["EOF"]):
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test an empty line, it should return False."""
        self.assertFalse(self.console.onecmd("\n"))

    def test_create(self):
        """Test the create command."""
        with patch('builtins.input', return_value="create BaseModel"):
            self.assertFalse(self.console.onecmd("create BaseModel"))

    def test_show(self):
        """Test the show command."""
        with patch('builtins.input', return_value="show BaseModel"):
            self.assertFalse(self.console.onecmd("show BaseModel"))

    def test_destroy(self):
        """Test the destroy command."""
        with patch('builtins.input', return_value="destroy BaseModel"):
            self.assertFalse(self.console.onecmd("destroy BaseModel"))

    def test_all(self):
        """Test the all command."""
        with patch('builtins.input', return_value="all"):
            self.assertFalse(self.console.onecmd("all"))

    def test_update(self):
        """Test the update command."""
        with patch('builtins.input', return_value="update BaseModel"):
            self.assertFalse(self.console.onecmd("update BaseModel"))

    def test_help_quit(self):
        """Test the help message for quit."""
        with patch('builtins.input', return_value="help quit"):
            self.assertFalse(self.console.onecmd("help quit"))

    def test_help_EOF(self):
        """Test the help message for EOF."""
        with patch('builtins.input', return_value="help EOF"):
            self.assertFalse(self.console.onecmd("help EOF"))

    def test_help_create(self):
        """Test the help message for create."""
        with patch('builtins.input', return_value="help create"):
            self.assertFalse(self.console.onecmd("help create"))

    def test_help_show(self):
        """Test the help message for show."""
        with patch('builtins.input', return_value="help show"):
            self.assertFalse(self.console.onecmd("help show"))

    def test_help_destroy(self):
        """Test the help message for destroy."""
        with patch('builtins.input', return_value="help destroy"):
            self.assertFalse(self.console.onecmd("help destroy"))

    def test_help_all(self):
        """Test the help message for all."""
        with patch('builtins.input', return_value="help all"):
            self.assertFalse(self.console.onecmd("help all"))

    def test_help_update(self):
        """Test the help message for update."""
        with patch('builtins.input', return_value="help update"):
            self.assertFalse(self.console.onecmd("help update"))

if __name__ == "__main__":
    unittest.main()

