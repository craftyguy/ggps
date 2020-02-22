
import inspect
import json
import sys
import time
import os

import ggps

if __name__ == "__main__":

    print('version {}'.format(ggps.VERSION))
    print(str(inspect.ismodule(ggps)))

    if False:
        infile = 'data/twin_cities_marathon.gpx'
        handler = ggps.GpxHandler()
        handler.parse(infile)
        trackpoints = handler.trackpoints
        count = len(trackpoints)
        print('{} trackpoints loaded from file {}'.format(count, infile))

    if False:
        infile = 'data/twin_cities_marathon.tcx'
        handler = ggps.TcxHandler()
        handler.parse(infile)
        trackpoints = handler.trackpoints
        count = len(trackpoints)
        print('{} trackpoints loaded from file {}'.format(count, infile))
        for t in trackpoints:
            print(repr(t))

    if True:
        infile = 'data/twin_cities_marathon.tcx'
        handler = ggps.PathHandler()
        handler.parse(infile)
        print(str(handler))
        obj = json.loads(str(handler))

    if False:
        infile = 'data/activity_4564516081.tcx'
        handler = ggps.TcxHandler()
        handler.parse(infile)
        trackpoints = handler.trackpoints
        count = len(trackpoints)
        print('{} trackpoints loaded from file {}'.format(count, infile))
        for t in trackpoints:
            print(repr(t))

    print('trackpoint count: {}'.format(len(trackpoints)))

