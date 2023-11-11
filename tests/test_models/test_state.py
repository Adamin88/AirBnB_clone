#!/usr/bin/python3

import unittest
import os
from models.state import State
from models.__init__ import storage
from console import HBNBCommand

class TestState(unittest.TestCase):
    def setUp(self):
        """Set up a clean testing environment."""
        self.state = State()
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
            objects_dict.pop("State." + self.test_id, None)
            with open(path, "w") as file:
                file.write(storage.all_to_json())

    def test_create_state(self):
        """Test creating a new State instance."""
        self.console.onecmd("create State")
        self.assertIn("State", storage.all())

    def test_show_state(self):
        """Test showing details of a State instance."""
        self.console.onecmd("create State")
        obj_id = list(storage.all("State").keys())[0]
        output = self.console.onecmd(f"show State {obj_id}")
        self.assertTrue(obj_id in output)

    def test_destroy_state(self):
        """Test destroying a State instance."""
        self.console.onecmd("create State")
        obj_id = list(storage.all("State").keys())[0]
        self.console.onecmd(f"destroy State {obj_id}")
        self.assertNotIn(obj_id, storage.all("State"))

    def test_all_state(self):
        """Test listing all State instances."""
        self.console.onecmd("create State")
        output = self.console.onecmd("all State")
        obj_id = list(storage.all("State").keys())[0]
        self.assertTrue(obj_id in output)

    def test_update_state(self):
        """Test updating a State instance."""
        self.console.onecmd("create State")
        obj_id = list(storage.all("State").keys())[0]
        self.test_id = obj_id
        self.console.onecmd(f"update State {obj_id} name 'California'")
        updated_state = storage.all("State")[obj_id]
        self.assertEqual(updated_state.name, "California")

if __name__ == "__main__":
    unittest.main()

