
import pytest

import ggps


def expected_first_trackpoint():
    return {
        "elapsedtime": "00:00:00",
        "heartratebpm": "85",
        "latitudedegrees": "44.97431952506304",
        "longitudedegrees": "-93.26310088858008",
        "seq": "1",
        "time": "2014-10-05T13:07:53.000Z",
        "type": "Trackpoint"
    }

def expected_middle_trackpoint():
    return {
        "elapsedtime": "03:13:19",
        "heartratebpm": "140",
        "latitudedegrees": "44.959017438814044",
        "longitudedegrees": "-93.21290854364634",
        "seq": "1747",
        "time": "2014-10-05T16:21:12.000Z",
        "type": "Trackpoint"
    }

def expected_last_trackpoint():
    return {
        "elapsedtime": "04:14:24",
        "heartratebpm": "161",
        "latitudedegrees": "44.95180849917233",
        "longitudedegrees": "-93.10493202880025",
        "seq": "2256",
        "time": "2014-10-05T17:22:17.000Z",
        "type": "Trackpoint"
    }

def test_twin_cities_marathon_gpx_file():
    filename = 'data/twin_cities_marathon.gpx'
    handler = ggps.GpxHandler()
    handler.parse(filename)

    tkpts = handler.trackpoints
    expected_attr_count = 7

    # check the number of trackpoints
    actual = len(tkpts)
    expected = 2256
    assert(actual == expected)

    # check the first trackpoint
    expected_tkpt = expected_first_trackpoint()
    actual_tkpt = handler.trackpoints[0]
    assert(len(actual_tkpt.values) == expected_attr_count)
    for key in expected_tkpt.keys():
        expected, actual = expected_tkpt[key], actual_tkpt.values[key]
        assert(expected == actual)

    # check a trackpoint at ~mile 20
    expected_tkpt = expected_middle_trackpoint()
    actual_tkpt = handler.trackpoints[1746]
    assert(len(actual_tkpt.values) == expected_attr_count)
    for key in expected_tkpt.keys():
        expected, actual = expected_tkpt[key], actual_tkpt.values[key]
        assert(expected == actual)

    # check the last trackpoint
    expected_tkpt = expected_last_trackpoint()
    actual_tkpt = handler.trackpoints[-1]
    assert(len(actual_tkpt.values) == expected_attr_count)
    for key in expected_tkpt.keys():
        expected, actual = expected_tkpt[key], actual_tkpt.values[key]
        assert(expected == actual)

    # check seconds_to_midnight
    secs = int(handler.first_time_secs_to_midnight)
    assert(secs > 0)
    assert(secs < 86400)
