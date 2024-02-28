#!/usr/bin/python3
"""Module for testing User class"""

import unittest
import os
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """User test cases"""

    def setUp(self):
        """Set up instances for tests"""
        self.obj1 = User()
        self.obj2 = User()

    def test_attr_init(self):
        """Test if attributes initialise as empty strings"""
        self.assertEqual(self.obj1.email, "")
        self.assertEqual(self.obj1.password, "")
        self.assertEqual(self.obj1.first_name, "")
        self.assertEqual(self.obj1.last_name, "")

    def test_id_creation(self):
        """Test if every user has a unique ID"""
        self.assertNotEqual(self.obj1.id, self.obj2.id)
        self.assertIsInstance(self.obj1.id, str)

    def test_instance(self):
        """Test if instances are of User"""
        self.assertIsInstance(self.obj1, User)
        self.assertIsInstance(self.obj2, User)

    def test_time_attrs(self):
        """Test if created_at and updated_at attributes are correctly set"""
        self.assertIsInstance(self.obj1.created_at, datetime)
        before_save = self.obj1.updated_at
        self.obj1.save()
        after_save = self.obj1.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_to_dict(self):
        """Test if to_dict method works properly"""
        user_dict = self.obj1.to_dict()
        format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(user_dict['created_at'],
                         self.obj1.created_at.strftime(format))
        self.assertEqual(user_dict['updated_at'],
                         self.obj1.updated_at.strftime(format))

    def test_file_permissions(self):
        """Test file permissions"""
        self.assertTrue(os.access('models/user.py', os.R_OK))
        self.assertTrue(os.access('models/user.py', os.W_OK))
        self.assertTrue(os.access('models/user.py', os.X_OK))

    def test_attr_type(self):
        """Test attribute types for BaseModel objects"""
        self.assertIsInstance(self.obj1.email, str)
        self.assertIsInstance(self.obj1.password, str)
        self.assertIsInstance(self.obj1.first_name, str)
        self.assertIsInstance(self.obj1.last_name, str)

    def test_inheritance(self):
        """Check if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_datetime_save(self):
        """Test datetime format"""
        crea_time = self.obj1.created_at
        self.obj1.save()
        upda_time = self.obj1.updated_at
        self.assertEqual(type(crea_time), datetime)
        self.assertEqual(type(upda_time), datetime)
        self.assertNotEqual(crea_time, upda_time)

    def test_module_doc(self):
        """Test module documentation"""
        self.assertTrue(len(User.__module__.strip()) > 0)

    def test_class_doc(self):
        """Test class documentation"""
        self.assertTrue(len(User.__doc__.strip()) > 0)

    def test_method_docs(self):
        """Test method documentation"""
        for method in dir(User):
            self.assertTrue(len(method.__doc__.strip()) > 0)

    def test_style_check(self):
        """Test pycodestyle"""
        style = os.system("pycodestyle models/user.py")
        self.assertEqual(style, 0)
