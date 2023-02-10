#!/usr/bin/python3
"""This module is meant to create an instance of Filestorage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
