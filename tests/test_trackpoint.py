
import json
import pytest

import ggps


def test_str():
    t = ggps.Trackpoint()
    assert(str(t) == '<Trackpoint values count:1>')

def test_repr():
    t = ggps.Trackpoint()
    t.set('lang', 'python')
    t.set(None, 'python')
    j = repr(t)
    obj = json.loads(j)
    assert(obj['type'] == 'Trackpoint')
    assert(obj['lang'] == 'python')

def test_get():
    t = ggps.Trackpoint()
    t.set('lang', 'python')
    assert(t.get('lang') == 'python')
    assert(t.get('xxx') == '')
    assert(t.get('zzz', 'zero') == 'zero')
