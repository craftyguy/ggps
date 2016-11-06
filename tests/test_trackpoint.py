
import unittest

import ggps


class TrackpointTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        t = ggps.Trackpoint()
        actual = str(t)
        expected = '<Trackpoint values count:1>'
        msg = "Should be {0}, got {1}".format(expected, actual)
        self.assertTrue(actual == expected, msg)

        t.set('k', 'v')
        self.assertTrue('v' == t.get('k'), 'Expected get to return v')
