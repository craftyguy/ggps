
import json
import unittest

import ggps


class TrackpointTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_str(self):
        t = ggps.Trackpoint()
        actual = str(t)
        expected = '<Trackpoint values count:1>'
        msg = "Should be {0}, got {1}".format(expected, actual)
        self.assertTrue(actual == expected, msg)

    def test_repr(self):
        t = ggps.Trackpoint()
        t.set('lang', 'python')
        t.set(None, 'python')
        j = repr(t)
        obj = json.loads(j)
        t = obj['type']
        l = obj['lang']
        self.assertTrue(t == 'Trackpoint', "expected the value 'Trackpoint'")
        self.assertTrue(l == 'python', "expected the value 'python'")

    def test_get(self):
        t = ggps.Trackpoint()
        t.set('lang', 'python')
        l = t.get('lang')
        x = t.get('xxx')
        z = t.get('zzz', 'zero')
        self.assertTrue(l == 'python', "expected the value 'python'")
        self.assertTrue(x == '', "expected the value ''")
        self.assertTrue(z == 'zero', "expected the value 'zero'")
