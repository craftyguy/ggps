
import unittest

import ggps


class GpxHandlerTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def expected_first_trackpoint(self):
        return {
          "elapsedtime": "00:00:00",
          "heartratebpm": "85",
          "latitudedegrees": "44.97431952506304",
          "longitudedegrees": "-93.26310088858008",
          "seq": "1",
          "time": "2014-10-05T13:07:53.000Z",
          "type": "Trackpoint"
        }

    def expected_middle_trackpoint(self):
        return {
          "elapsedtime": "03:13:19",
          "heartratebpm": "140",
          "latitudedegrees": "44.959017438814044",
          "longitudedegrees": "-93.21290854364634",
          "seq": "1747",
          "time": "2014-10-05T16:21:12.000Z",
          "type": "Trackpoint"
        }

    def expected_last_trackpoint(self):
        return {
          "elapsedtime": "04:14:24",
          "heartratebpm": "161",
          "latitudedegrees": "44.95180849917233",
          "longitudedegrees": "-93.10493202880025",
          "seq": "2256",
          "time": "2014-10-05T17:22:17.000Z",
          "type": "Trackpoint"
        }

    def test_twin_cities_marathon_gpx_file(self):
        filename = 'data/twin_cities_marathon.gpx'
        handler = ggps.GpxHandler.parse(filename, True)
        tkpts = handler.trackpoints

        actual = len(tkpts)
        expected = 2256
        msg = "Should be {0} trackpoints, got {1}".format(expected, actual)
        self.assertTrue(actual == expected, msg)


        self.assertTrue(tkpts[0] == self.expected_first_trackpoint())



    # def test_milliseconds_per_year(self):
    #     self.assertTrue(m26.AgeCalculator.milliseconds_per_year() == 31557600000.0, "value should be 31557600000.0")
    #
    # def test_calculate(self):
    #     a1 = m26.AgeCalculator.calculate('1960-10-01', '2015-10-01')
    #     actual = 54.997946611909654
    #     self.assertTrue(a1.value > (actual - 0.000001), "value is too small")
    #     self.assertTrue(a1.value < (actual + 0.000001), "value is too large")
