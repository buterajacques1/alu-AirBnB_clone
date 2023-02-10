import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        self.assertIsInstance(str(self.base_model), str)

    def test_save(self):
        previous_update_time = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_update_time, self.base_model.updated_at)

    def test_to_dict(self):
        dictionary = self.base_model.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary["__class__"], "BaseModel")
        self.assertIsInstance(dictionary["created_at"], str)
        self.assertIsInstance(dictionary["updated_at"], str)


if __name__ == "__main__":

    unittest.main()
