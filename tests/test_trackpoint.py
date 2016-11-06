
import unittest

import ggps

class TrackpointTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_twin_cities_marathon_gpx_file(self):
        t = ggps.Trackpoint()
        actual = str(t)
        expected = '<Trackpoint values count:1>'
        msg = "Should be {0}, got {1}".format(expected, actual)
        self.assertTrue(actual == expected, msg)
