#!/usr/bin/python3

import unittest
import os
from models.user import User
from models.__init__ import storage
from console import HBNBCommand


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up a clean testing environment."""
        self.user = User()
        self.console = HBNBCommand()
        self.test_id = None

    def tearDown(self):
        """Clean up resources after testing."""
        if self.test_id:
            path = "file.json"
            with open(path, "r") as file:
                content = file.read()
            storage.reload()
            objects_dict = storage.all()
            objects_dict.pop("User." + self.test_id, None)
            with open(path, "w") as file:
                file.write(storage.all_to_json())

    def test_create_user(self):
        """Test creating a new User instance."""
        self.console.onecmd("create User")
        self.assertIn("User", storage.all())

    def test_show_user(self):
        """Test showing details of a User instance."""
        self.console.onecmd("create User")
        obj_id = list(storage.all("User").keys())[0]
        output = self.console.onecmd(f"show User {obj_id}")
        self.assertTrue(obj_id in output)

    def test_destroy_user(self):
        """Test destroying a User instance."""
        self.console.onecmd("create User")
        obj_id = list(storage.all("User").keys())[0]
        self.console.onecmd(f"destroy User {obj_id}")
        self.assertNotIn(obj_id, storage.all("User"))

    def test_all_user(self):
        """Test listing all User instances."""
        self.console.onecmd("create User")
        output = self.console.onecmd("all User")
        obj_id = list(storage.all("User").keys())[0]
        self.assertTrue(obj_id in output)

    def test_update_user(self):
        """Test updating a User instance."""
        self.console.onecmd("create User")
        obj_id = list(storage.all("User").keys())[0]
        self.test_id = obj_id
        self.console.onecmd(f"update User {obj_id} name 'John Doe'")
        updated_user = storage.all("User")[obj_id]
        self.assertEqual(updated_user.name, "John Doe")


if __name__ == "__main__":
    unittest.main()
