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
