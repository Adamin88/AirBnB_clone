#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from models.__init__ import storage
from console import HBNBCommand

class TestBaseModelDict(unittest.TestCase):
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

    def test_to_dict_base_model(self):
        """Test the to_dict() method of BaseModel."""
        obj_id = self.base_model.id
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        base_model_dict = self.base_model.to_dict()

        self.assertEqual(set(base_model_dict.keys()), set(expected_keys))
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], obj_id)

    def test_save_reload_to_dict(self):
        """Test saving, reloading, and checking to_dict() consistency."""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all("BaseModel").keys())[0]
        self.test_id = obj_id
        path = "file.json"
        
        with open(path, "r") as file:
            content = file.read()

        storage.reload()
        loaded_objects_dict = storage.all()
        loaded_base_model_dict = loaded_objects_dict["BaseModel." + obj_id].to_dict()

        self.assertEqual(loaded_base_model_dict['id'], obj_id)
        self.assertEqual(loaded_base_model_dict['__class__'], 'BaseModel')

if __name__ == "__main__":
    unittest.main()

