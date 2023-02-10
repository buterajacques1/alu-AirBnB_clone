import unittest
from datetime import datetime
import models
import uuid

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = models.BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model, models.BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        expected_str = '[BaseModel] ({}) {{'format(self.model.id)
        expected_str += "'id': '{}', ".format(self.model.id)
        expected_str += "'created_at': {}, ".format(repr(self.model.created_at))
        expected_str += "'updated_at': {}}}".format(repr(self.model.updated_at))
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
