#!/usr/bin/python3

import unittest
import os
from models.amenity import Amenity
from models.__init__ import storage
from console import HBNBCommand

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up a clean testing environment."""
        self.amenity = Amenity()
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
            objects_dict.pop("Amenity." + self.test_id, None)
            with open(path, "w") as file:
                file.write(storage.all_to_json())
        
    def test_create_amenity(self):
        """Test creating a new Amenity instance."""
        self.console.onecmd("create Amenity")
        self.assertIn("Amenity", storage.all())

    def test_show_amenity(self):
        """Test showing details of an Amenity instance."""
        self.console.onecmd("create Amenity")
        obj_id = list(storage.all("Amenity").keys())[0]
        output = self.console.onecmd(f"show Amenity {obj_id}")
        self.assertTrue(obj_id in output)

    def test_destroy_amenity(self):
        """Test destroying an Amenity instance."""
        self.console.onecmd("create Amenity")
        obj_id = list(storage.all("Amenity").keys())[0]
        self.console.onecmd(f"destroy Amenity {obj_id}")
        self.assertNotIn(obj_id, storage.all("Amenity"))

    def test_all_amenity(self):
        """Test listing all Amenity instances."""
        self.console.onecmd("create Amenity")
        output = self.console.onecmd("all Amenity")
        obj_id = list(storage.all("Amenity").keys())[0]
        self.assertTrue(obj_id in output)

    def test_update_amenity(self):
        """Test updating an Amenity instance."""
        self.console.onecmd("create Amenity")
        obj_id = list(storage.all("Amenity").keys())[0]
        self.test_id = obj_id
        self.console.onecmd(f"update Amenity {obj_id} name testing")
        updated_amenity = storage.all("Amenity")[obj_id]
        self.assertEqual(updated_amenity.name, "testing")

if __name__ == "__main__":
    unittest.main()

