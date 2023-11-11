#!/usr/bin/python3
"""
Module for the FileStorage class
"""
import json

class FileStorage:
    """
    The FileStorage class manages the serialization and deserialization
    of instances to and from JSON files.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the file exists).
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                cls_name = value['__class__']
                cls = models.classes[cls_name]
                obj = cls(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
