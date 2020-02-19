
import pytest

import ggps


def test_author():
    value = ggps.__author__
    assert(value == 'cjoakim')

def test_version():
    value = ggps.VERSION
    assert(value == '0.2.1')
