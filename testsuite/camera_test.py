#!/usr/bin/env python3
"""
Testing camera module
"""
import unittest
import sys
import os

sys.path.insert(0, os.getcwd())
from lib.camera import Camera
from lib.config import REGISTRATION_FOLDER


class TestCamera(unittest.TestCase):
    """
    Test for the Camera class
    """
    @classmethod
    def setUpClass(cls):
        """
        Initialize camera
        """
        cls.camera = Camera(REGISTRATION_FOLDER)

    def setUp(self) -> None:
        """
        Create file in REGISTRATION_FOLDER
        """
        open(REGISTRATION_FOLDER + "tests.txt", 'a').close()

    def test_recording(self):
        """
        Test method camera.start_recording()
        """
        video = self.camera.start_recording(10)
        self.assertEqual(video["return_code"], None,
                         "ERROR: during recording video[\"return_code\"]")

    def test_take_photo(self):
        """
        Test method camera.take_photo()
        """
        photo = self.camera.take_photo()
        self.assertTrue(os.path.isfile(photo))

    def test_purge_folder(self):
        """
        Test method camera.purge_records()
        """
        self.assertEqual(self.camera.purge_records(),
                         'The records have been deleted',
                         "purge_record doesn't function")


if __name__ == '__main__':
    unittest.main()
