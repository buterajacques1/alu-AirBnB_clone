import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Defines tests for the BaseModel class"""

    def setUp(self):
        """Sets up the test environment"""
        self.base_model = BaseModel()

    def test_id(self):
        """Tests the id attribute"""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """Tests the created_at attribute"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Tests the updated_at attribute"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """Tests the __str__ method"""
        s = str(self.base_model)
        self.assertIsInstance(s, str)
        self.assertIn("[BaseModel]", s)
        self.assertIn("id", s)
        self.assertIn("created_at", s)
        self.assertIn("updated_at", s)

    def test_save(self):
        """Tests the save method"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method"""
        d = self.base_model.to_dict()
        self.assertIsInstance(d, dict)
        self.assertIn('__class__', d)
        self.assertIn('id', d)
        self.assertIn('created_at', d)
        self.assertIn('updated_at', d)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['id'], self.base_model.id)
        self.assertEqual(d['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(d['updated_at'], self.base_model.updated_at.isoformat())
