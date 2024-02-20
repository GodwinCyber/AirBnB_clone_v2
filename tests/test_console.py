#!/usr/bin/python3
"""test console"""
import os
import uuid
import models
import unittest
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from model.engine.db_storage import DBStorage
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """test HBNB command interpreter"""

    @classmethod
    def setUpClass(test_cls):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        test_cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(test_cls):
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        del test_cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage_session.close()

    def setUp(self):
        FileStorage._FileStorage_objects = {}
    
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
