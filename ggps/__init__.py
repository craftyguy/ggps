__author__ = 'cjoakim'
__version__ = '0.1.8'

"""
ggps library
"""

VERSION = __version__

from .trackpoint import Trackpoint
from .base_handler import BaseHandler
from .gpx_handler import GpxHandler
from .path_handler import PathHandler
from .tcx_handler import TcxHandler

print('imported ggps')
