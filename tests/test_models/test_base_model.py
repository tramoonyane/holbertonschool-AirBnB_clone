#!/usr/bin/python3
"""Unit tests for AirBnB project's BaseModel class."""
import unittest
import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """BaseModel test cases"""

    def setUp(self):
        """Set up testing environment"""
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()

    def tearDown(self):
        """Teardown testing environment"""
        del self.obj1
        del self.obj2

    def test_instance(self):
        """Check if instance is a type of BaseModel"""
        self.assertIsInstance(self.obj1, BaseModel)

    def test_unique_id(self):
        """Ensure that the IDs are unique"""
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_attrs_existence(self):
        """Check if attributes are correctly set"""
        self.obj1.name = "test name"
        self.assertEqual(self.obj1.name, "test name")
        self.obj1.number = 3
        self.assertEqual(self.obj1.number, 3)

    def test_default_attr_values(self):
        """Ensure default attributes are set"""
        self.assertIsNotNone(self.obj1.id)
        self.assertIsNotNone(self.obj1.created_at)
        self.assertIsNotNone(self.obj1.updated_at)

    def test_to_dict_return_type(self):
        """Check if to_dict returns a dictionary with expected keys"""
        obj_dict = self.obj1.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in obj_dict)

    def test_to_dict_values(self):
        """Validate values in the dictionary representation"""
        obj = BaseModel()
        expec_dict = obj.__dict__.copy()
        expec_dict['__class__'] = type(obj).__name__
        expec_dict['created_at'] = obj.created_at.isoformat()
        expec_dict['updated_at'] = obj.updated_at.isoformat()
        self.assertDictEqual(expec_dict, obj.to_dict())

    def test_datetime_conversion(self):
        """Check if datetime is converted to a string"""
        obj_dict = self.obj1.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_updated_at_is_greater(self):
        """Ensure updated_at is greater than created_at after save"""
        obj = BaseModel()
        time.sleep(1)
        obj.save()
        self.assertTrue(obj.created_at < obj.updated_at)

    def test_updated_at_changes_after_save(self):
        """Check if updated_at changes after save"""
        obj = BaseModel()
        first_time = obj.updated_at
        time.sleep(1)
        obj.save()
        updated_time = obj.updated_at
        self.assertNotEqual(first_time, updated_time)

    def test_updated_at_datetime(self):
        """Test if it changes after save"""
        ori_time = self.obj1.updated_at
        self.obj1.save()
        new_time = self.obj1.updated_at
        self.assertNotEqual(ori_time, new_time)

    def test_str_representation(self):
        """Test the string representation"""
        obj_type = type(self.obj1).__name__
        obj_str = f"[{obj_type}] ({self.obj1.id}) {self.obj1.__dict__}"
        self.assertEqual(str(self.obj1), obj_str)

    def test_class_attr(self):
        """Ensure __class__ isn't added as an instance attribute."""
        obj = BaseModel(__class__="SomeClass")
        self.assertNotEqual(obj.__class__, "SomeClass")

    def test_datetime_from_kwargs(self):
        """Ensure created_at is processed correctly from keyword arguments"""
        obj = BaseModel(created_at="2002-10-25T15:45:00.000001")
        self.assertIsInstance(obj.created_at, datetime.datetime)

    def test_init_with_kwargs(self):
        obj = BaseModel(
            id="unique_id",
            created_at="2002-10-25T15:45:00.000001",
            updated_at="2002-10-25T15:45:00.000001"
        )
        expected_dict = {
            "__class__": "BaseModel",
            "id": "unique_id",
            "created_at": "2002-10-25T15:45:00.000001",
            "updated_at": "2002-10-25T15:45:00.000001"
        }
        self.assertEqual(obj.to_dict(), expected_dict)
