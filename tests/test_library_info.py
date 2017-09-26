
import unittest

import ggps


class LibraryInfoTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_author(self):
        value = ggps.__author__
        self.assertTrue(value == 'cjoakim', "author is incorrect")

    def test_version(self):
        value = ggps.VERSION
        self.assertTrue(value == '0.1.13', "VERSION is incorrect")
