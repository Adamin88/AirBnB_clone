#!/usr/bin/python3

import unittest
import os
from models.place import Place
from models.__init__ import storage
from console import HBNBCommand


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up a clean testing environment."""
        self.place = Place()
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
            objects_dict.pop("Place." + self.test_id, None)
            with open(path, "w") as file:
                file.write(storage.all_to_json())

    def test_create_place(self):
        """Test creating a new Place instance."""
        self.console.onecmd("create Place")
        self.assertIn("Place", storage.all())

    def test_show_place(self):
        """Test showing details of a Place instance."""
        self.console.onecmd("create Place")
        obj_id = list(storage.all("Place").keys())[0]
        output = self.console.onecmd(f"show Place {obj_id}")
        self.assertTrue(obj_id in output)

    def test_destroy_place(self):
        """Test destroying a Place instance."""
        self.console.onecmd("create Place")
        obj_id = list(storage.all("Place").keys())[0]
        self.console.onecmd(f"destroy Place {obj_id}")
        self.assertNotIn(obj_id, storage.all("Place"))

    def test_all_place(self):
        """Test listing all Place instances."""
        self.console.onecmd("create Place")
        output = self.console.onecmd("all Place")
        obj_id = list(storage.all("Place").keys())[0]
        self.assertTrue(obj_id in output)

    def test_update_place(self):
        """Test updating a Place instance."""
        self.console.onecmd("create Place")
        obj_id = list(storage.all("Place").keys())[0]
        self.test_id = obj_id
        self.console.onecmd(f"update Place {obj_id} name testing")
        updated_place = storage.all("Place")[obj_id]
        self.assertEqual(updated_place.name, "testing")


if __name__ == "__main__":
    unittest.main()
