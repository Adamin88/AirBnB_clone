#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.__init__ import storage
from console import HBNBCommand

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up a clean testing environment."""
        self.base_model = BaseModel()
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
            objects_dict.pop("BaseModel." + self.test_id, None)
            with open(path, "w") as file:
                file.write(storage.all_to_json())

    def test_create_base_model(self):
        """Test creating a new BaseModel instance."""
        self.console.onecmd("create BaseModel")
        self.assertIn("BaseModel", storage.all())

    def test_show_base_model(self):
        """Test showing details of a BaseModel instance."""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all("BaseModel").keys())[0]
        output = self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertTrue(obj_id in output)

    def test_destroy_base_model(self):
        """Test destroying a BaseModel instance."""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all("BaseModel").keys())[0]
        self.console.onecmd(f"destroy BaseModel {obj_id}")
        self.assertNotIn(obj_id, storage.all("BaseModel"))

    def test_all_base_model(self):
        """Test listing all BaseModel instances."""
        self.console.onecmd("create BaseModel")
        output = self.console.onecmd("all BaseModel")
        obj_id = list(storage.all("BaseModel").keys())[0]
        self.assertTrue(obj_id in output)

    def test_update_base_model(self):
        """Test updating a BaseModel instance."""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all("BaseModel").keys())[0]
        self.test_id = obj_id
        self.console.onecmd(f"update BaseModel {obj_id} name 'Test Model'")
        updated_base_model = storage.all("BaseModel")[obj_id]
        self.assertEqual(updated_base_model.name, "Test Model")

if __name__ == "__main__":
    unittest.main()

