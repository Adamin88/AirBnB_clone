#!/usr/bin/python3

import unittest
import os
from models.city import City
from models.__init__ import storage
from console import HBNBCommand


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up a clean testing environment."""
        self.city = City()
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
            objects_dict.pop("City." + self.test_id, None)
            with open(path, "w") as file:
                file.write(storage.all_to_json())

    def test_create_city(self):
        """Test creating a new City instance."""
        self.console.onecmd("create City")
        self.assertIn("City", storage.all())

    def test_show_city(self):
        """Test showing details of a City instance."""
        self.console.onecmd("create City")
        obj_id = list(storage.all("City").keys())[0]
        output = self.console.onecmd(f"show City {obj_id}")
        self.assertTrue(obj_id in output)

    def test_destroy_city(self):
        """Test destroying a City instance."""
        self.console.onecmd("create City")
        obj_id = list(storage.all("City").keys())[0]
        self.console.onecmd(f"destroy City {obj_id}")
        self.assertNotIn(obj_id, storage.all("City"))

    def test_all_city(self):
        """Test listing all City instances."""
        self.console.onecmd("create City")
        output = self.console.onecmd("all City")
        obj_id = list(storage.all("City").keys())[0]
        self.assertTrue(obj_id in output)

    def test_update_city(self):
        """Test updating a City instance."""
        self.console.onecmd("create City")
        obj_id = list(storage.all("City").keys())[0]
        self.test_id = obj_id
        self.console.onecmd(f"update City {obj_id} name testing")
        updated_city = storage.all("City")[obj_id]
        self.assertEqual(updated_city.name, "testing")


if __name__ == "__main__":
    unittest.main()
