#!/usr/bin/python3

import unittest
import os
from models.review import Review
from models.__init__ import storage
from console import HBNBCommand


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up a clean testing environment."""
        self.review = Review()
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
            objects_dict.pop("Review." + self.test_id, None)
            with open(path, "w") as file:
                file.write(storage.all_to_json())

    def test_create_review(self):
        """Test creating a new Review instance."""
        self.console.onecmd("create Review")
        self.assertIn("Review", storage.all())

    def test_show_review(self):
        """Test showing details of a Review instance."""
        self.console.onecmd("create Review")
        obj_id = list(storage.all("Review").keys())[0]
        output = self.console.onecmd(f"show Review {obj_id}")
        self.assertTrue(obj_id in output)

    def test_destroy_review(self):
        """Test destroying a Review instance."""
        self.console.onecmd("create Review")
        obj_id = list(storage.all("Review").keys())[0]
        self.console.onecmd(f"destroy Review {obj_id}")
        self.assertNotIn(obj_id, storage.all("Review"))

    def test_all_review(self):
        """Test listing all Review instances."""
        self.console.onecmd("create Review")
        output = self.console.onecmd("all Review")
        obj_id = list(storage.all("Review").keys())[0]
        self.assertTrue(obj_id in output)

    def test_update_review(self):
        """Test updating a Review instance."""
        self.console.onecmd("create Review")
        obj_id = list(storage.all("Review").keys())[0]
        self.test_id = obj_id
        self.console.onecmd(f"update Review {obj_id} text 'Great review'")
        updated_review = storage.all("Review")[obj_id]
        self.assertEqual(updated_review.text, "Great review")


if __name__ == "__main__":
    unittest.main()
