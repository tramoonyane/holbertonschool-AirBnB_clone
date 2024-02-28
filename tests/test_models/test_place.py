#!/usr/bin/python3
"""Module for testing Place class"""

import unittest
import os
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Place test cases"""

    def setUp(self):
        """Setting up the objects for testing"""
        self.obj1 = Place()
        self.obj2 = Place()

    def test_instance(self):
        """Test if instances are of Place"""
        self.assertIsInstance(self.obj1, Place)
        self.assertIsInstance(self.obj2, Place)

    def test_id_creation(self):
        """Test if the IDs of two objects are different"""
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_attr_init(self):
        """Test if attributes initialise correctly"""
        self.assertEqual(self.obj1.city_id, "")
        self.assertEqual(self.obj1.user_id, "")
        self.assertEqual(self.obj1.name, "")
        self.assertEqual(self.obj1.description, "")
        self.assertEqual(self.obj1.number_rooms, 0)
        self.assertEqual(self.obj1.number_bathrooms, 0)
        self.assertEqual(self.obj1.max_guest, 0)
        self.assertEqual(self.obj1.price_by_night, 0)
        self.assertEqual(self.obj1.latitude, 0.0)
        self.assertEqual(self.obj1.longitude, 0.0)
        self.assertEqual(self.obj1.amenity_ids, [])

    def test_time_attrs(self):
        """Test if created_at and updated_at attributes are correctly set"""
        self.assertEqual(self.obj1.created_at, self.obj1.updated_at)
        self.assertTrue(isinstance(self.obj1.created_at, datetime))

    def test_attr_types(self):
        """Test attribute types for Place objects"""
        self.assertIsInstance(self.obj1.city_id, str)
        self.assertIsInstance(self.obj1.user_id, str)
        self.assertIsInstance(self.obj1.name, str)
        self.assertIsInstance(self.obj1.description, str)
        self.assertIsInstance(self.obj1.number_rooms, int)
        self.assertIsInstance(self.obj1.number_bathrooms, int)
        self.assertIsInstance(self.obj1.max_guest, int)
        self.assertIsInstance(self.obj1.price_by_night, int)
        self.assertIsInstance(self.obj1.latitude, float)
        self.assertIsInstance(self.obj1.longitude, float)
        self.assertIsInstance(self.obj1.amenity_ids, list)
        self.assertIsInstance(self.obj1.id, str)
        self.assertIsInstance(self.obj1.created_at, datetime)
        self.assertIsInstance(self.obj1.updated_at, datetime)

    def test_inheritance(self):
        """Check if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_datetime_save(self):
        """Test datetime format"""
        crea_time = self.obj1.created_at
        self.obj1.save()
        upda_time = self.obj1.updated_at
        self.assertEqual(type(crea_time), datetime)
        self.assertEqual(type(upda_time), datetime)
        self.assertNotEqual(crea_time, upda_time)

    def test_to_dict(self):
        """Test if to_dict method works properly for Place instances"""
        place_dict = self.obj1.to_dict()
        format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(place_dict['created_at'],
                         self.obj1.created_at.strftime(format))
        self.assertEqual(place_dict['updated_at'],
                         self.obj1.updated_at.strftime(format))

    def test_permissions(self):
        """Test file permissions"""
        self.assertTrue(os.access('models/place.py', os.R_OK))
        self.assertTrue(os.access('models/place.py', os.W_OK))
        self.assertTrue(os.access('models/place.py', os.X_OK))

    def test_module_doc(self):
        """Test module documentation"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_class_doc(self):
        """Test class documentation"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method_docs(self):
        """Test method documentation"""
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)

    def test_style_check(self):
        """Test pycodestyle"""
        style = os.system("pycodestyle models/place.py")
        self.assertEqual(style, 0)
