#!/usr/bin/python3
"""
Package initializer for the models module
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
