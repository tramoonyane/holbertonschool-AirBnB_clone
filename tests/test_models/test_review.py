#!/usr/bin/python3
"""Module for testing Review class"""

import unittest
import os
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Review test cases"""

    def setUp(self):
        """Setting up the objects for testing"""
        self.obj1 = Review()
        self.obj2 = Review()

    def test_instance(self):
        """Test if instances are of Review"""
        self.assertIsInstance(self.obj1, Review)
        self.assertIsInstance(self.obj2, Review)

    def test_id_creation(self):
        """Test if the IDs of two objects are different"""
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_attr_init(self):
        """Test if attributes initialise as empty strings and correct types"""
        self.assertEqual(self.obj1.place_id, "")
        self.assertEqual(self.obj1.user_id, "")
        self.assertEqual(self.obj1.text, "")
        self.assertIsInstance(self.obj1.place_id, str)
        self.assertIsInstance(self.obj1.user_id, str)
        self.assertIsInstance(self.obj1.text, str)

    def test_time_attrs(self):
        """Test if created_at and updated_at attributes are correctly set"""
        self.assertEqual(self.obj1.created_at, self.obj1.updated_at)
        self.assertTrue(isinstance(self.obj1.created_at, datetime))

    def test_attr_types(self):
        """Test attribute types for BaseModel objects"""
        self.assertIsInstance(self.obj1.place_id, str)
        self.assertIsInstance(self.obj1.user_id, str)
        self.assertIsInstance(self.obj1.text, str)
        self.assertIsInstance(self.obj1.id, str)
        self.assertIsInstance(self.obj1.created_at, datetime)
        self.assertIsInstance(self.obj1.updated_at, datetime)

    def test_inheritance(self):
        """Check if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_datetime_save(self):
        """Test datetime format"""
        crea_time = self.obj1.created_at
        self.obj1.save()
        upda_time = self.obj1.updated_at
        self.assertEqual(type(crea_time), datetime)
        self.assertEqual(type(upda_time), datetime)
        self.assertNotEqual(crea_time, upda_time)

    def test_to_dict(self):
        """Test if to_dict method works properly for Review instances"""
        review_dict = self.obj1.to_dict()
        format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(review_dict['created_at'],
                         self.obj1.created_at.strftime(format))
        self.assertEqual(review_dict['updated_at'],
                         self.obj1.updated_at.strftime(format))

    def test_permissions(self):
        """Test file permissions"""
        self.assertTrue(os.access('models/review.py', os.R_OK))
        self.assertTrue(os.access('models/review.py', os.W_OK))
        self.assertTrue(os.access('models/review.py', os.X_OK))

    def test_module_doc(self):
        """Test module documentation"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_class_doc(self):
        """Test class documentation"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method_docs(self):
        """Test method documentation"""
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)

    def test_style_check(self):
        """Test pycodestyle"""
        style = os.system("pycodestyle models/review.py")
        self.assertEqual(style, 0)
