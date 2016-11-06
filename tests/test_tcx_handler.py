
import unittest

import ggps


class TcxHandlerTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def expected_first_trackpoint(self):
        return {
            "altitudefeet": "850.3937408367167",
            "altitudemeters": "259.20001220703125",
            "distancekilometers": "0.0",
            "distancemeters": "0.0",
            "distancemiles": "0.0",
            "elapsedtime": "00:00:00",
            "heartratebpm": "85",
            "latitudedegrees": "44.97431952506304",
            "longitudedegrees": "-93.26310088858008",
            "runcadence": "89",
            "runcadencex2": "178",
            "seq": "1",
            "speed": "0.0",
            "time": "2014-10-05T13:07:53.000Z",
            "type": "Trackpoint"
        }

    def expected_middle_trackpoint(self):
        return {
            "altitudefeet": "805.7742982398804",
            "altitudemeters": "245.60000610351562",
            "distancekilometers": "32.187189453125",
            "distancemeters": "32187.189453125",
            "distancemiles": "20.00019228525722",
            "elapsedtime": "03:13:19",
            "heartratebpm": "140",
            "latitudedegrees": "44.959017438814044",
            "longitudedegrees": "-93.21290854364634",
            "runcadence": "84",
            "runcadencex2": "168",
            "seq": "1747",
            "speed": "2.8269999027252193",
            "time": "2014-10-05T16:21:12.000Z",
            "type": "Trackpoint"
        }

    def expected_last_trackpoint(self):
        return {
            "altitudefeet": "864.8294163501167",
            "altitudemeters": "263.6000061035156",
            "distancekilometers": "42.63544921875",
            "distancemeters": "42635.44921875",
            "distancemiles": "26.492439912628992",
            "elapsedtime": "04:14:24",
            "heartratebpm": "161",
            "latitudedegrees": "44.95180849917233",
            "longitudedegrees": "-93.10493202880025",
            "runcadence": "77",
            "runcadencex2": "154",
            "seq": "2256",
            "speed": "3.5460000038146977",
            "time": "2014-10-05T17:22:17.000Z",
            "type": "Trackpoint"
        }

    def test_twin_cities_marathon_gpx_file(self):
        filename = 'data/twin_cities_marathon.tcx'
        handler = ggps.TcxHandler.parse(filename)

        tkpts = handler.trackpoints
        expected_attr_count = 15

        self.assertTrue(handler.curr_depth() == 0, 'curr_depth should be 0')
        self.assertTrue(handler.curr_path() == '', 'curr_depth should be empty')

        # check the number of trackpoints
        actual = len(tkpts)
        expected = 2256
        msg = "Should be {0} trackpoints, got {1}".format(expected, actual)
        self.assertTrue(actual == expected, msg)
        actual = handler.trackpoint_count()
        self.assertTrue(actual == expected, msg)

        # check the first trackpoint
        expected_tkpt = self.expected_first_trackpoint()
        actual_tkpt = handler.trackpoints[0]
        self.assertTrue(len(actual_tkpt.values) == expected_attr_count)
        for key in expected_tkpt.keys():
            expected, actual = expected_tkpt[key], actual_tkpt.values[key]
            self.assertTrue(expected == actual, "first tkpt, key {0}".format(key))

        # check a trackpoint at ~mile 20
        expected_tkpt = self.expected_middle_trackpoint()
        actual_tkpt = handler.trackpoints[1746]
        self.assertTrue(len(actual_tkpt.values) == expected_attr_count)
        for key in expected_tkpt.keys():
            expected, actual = expected_tkpt[key], actual_tkpt.values[key]
            self.assertTrue(expected == actual, "20m tkpt, key {0}".format(key))

        # check the last trackpoint
        expected_tkpt = self.expected_last_trackpoint()
        actual_tkpt = handler.trackpoints[-1]
        self.assertTrue(len(actual_tkpt.values) == expected_attr_count)
        for key in expected_tkpt.keys():
            expected, actual = expected_tkpt[key], actual_tkpt.values[key]
            self.assertTrue(expected == actual, "last tkpt, key {0}".format(key))

        # check seconds_to_midnight
        secs = int(handler.first_time_secs_to_midnight)
        self.assertTrue(secs > 0, "first_time_secs_to_midnight is too small")
        self.assertTrue(secs < 86400, "first_time_secs_to_midnight is too large")
