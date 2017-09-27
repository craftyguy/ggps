
import json
import pytest

import ggps


def test_str():
    handler = ggps.PathHandler()
    actual = str(handler)
    expected = '{}'
    assert(actual == expected)

    filename = 'data/twin_cities_marathon.gpx'
    handler = ggps.PathHandler()
    handler.parse(filename)
    obj = json.loads(str(handler))
    cnt = obj['gpx|trk|trkseg|trkpt@lat']
    assert(cnt == 2256)

def test_counts():
    filename = 'data/twin_cities_marathon.gpx'
    handler = ggps.PathHandler()
    handler.parse(filename)
    counter = handler.path_counter
    cnt = counter['gpx|trk|trkseg|trkpt@lat']
    assert(cnt == 2256)
    cnt = counter['gpx|metadata|time']
    assert(cnt == 1)

def test_base_parse_hhmmss():
    filename = 'data/twin_cities_marathon.gpx'
    handler = ggps.PathHandler()
    handler.parse(filename)
    hhmmss = handler.parse_hhmmss('')
    assert(hhmmss == '')
    hhmmss = handler.parse_hhmmss('xxx')
    assert(hhmmss == '')
