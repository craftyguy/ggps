__author__ = 'cjoakim'
__version__ = '0.2.0'

"""
ggps library
"""

VERSION = __version__

import json
import m26
import xml.sax

from collections import defaultdict

from ggps.trackpoint import *
from ggps.base_handler import *
from ggps.gpx_handler import *
from ggps.path_handler import *
from ggps.tcx_handler import *
