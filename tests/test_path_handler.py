
import json
import unittest

import ggps


class PathHandlerTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_str(self):
        handler = ggps.PathHandler()
        actual = str(handler)
        expected = '{}'
        msg = "Should be {0}, got {1}".format(expected, actual)
        self.assertTrue(actual == expected, msg)

        filename = 'data/twin_cities_marathon.gpx'
        handler = ggps.PathHandler()
        handler.parse(filename)
        obj = json.loads(str(handler))
        cnt = obj['gpx|trk|trkseg|trkpt@lat']
        msg = "count of 2256 expected at 'gpx|trk|trkseg|trkpt@lat'"
        self.assertTrue(cnt == 2256, msg)

    def test_counts(self):
        filename = 'data/twin_cities_marathon.gpx'
        handler = ggps.PathHandler()
        handler.parse(filename)
        counter = handler.path_counter

        cnt = counter['gpx|trk|trkseg|trkpt@lat']
        msg = "count of 2256 expected at 'gpx|trk|trkseg|trkpt@lat'"
        self.assertTrue(cnt == 2256, msg)

        cnt = counter['gpx|metadata|time']
        msg = "count of 1 expected at 'gpx|metadata|time'"
        self.assertTrue(cnt == 1, msg)

    def test_base_parse_hhmmss(self):
        filename = 'data/twin_cities_marathon.gpx'
        handler = ggps.PathHandler()
        handler.parse(filename)

        hhmmss = handler.parse_hhmmss('')
        self.assertTrue(hhmmss == '', 'an empty hhmmss str was expected')

        hhmmss = handler.parse_hhmmss('xxx')
        self.assertTrue(hhmmss == '', 'an empty hhmmss str was expected')