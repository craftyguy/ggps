
import inspect
import json
import sys
import time
import os

import ggps

# python ggps-examples.py > data/ggps-examples.txt


if __name__ == "__main__":

    print('version {}'.format(ggps.VERSION))
    print(str(inspect.ismodule(ggps)))

    if True:
        infile = 'data/twin_cities_marathon.tcx'
        handler = ggps.PathHandler()
        handler.parse(infile)
        print(str(handler))
        obj = json.loads(str(handler))

    if True:
        infile = 'data/twin_cities_marathon.tcx'
        handler = ggps.TcxHandler()
        handler.parse(infile)
        trackpoints = handler.trackpoints
        count = len(trackpoints)
        print('{} trackpoints loaded from file {}'.format(count, infile))
        for t in trackpoints:
            print(repr(t))
        print('---')
        print(repr(trackpoints[-1]))
        print('{} trackpoints loaded from file {}'.format(count, infile))

    if True:
        infile = 'data/twin_cities_marathon.gpx'
        handler = ggps.GpxHandler()
        handler.parse(infile)
        trackpoints = handler.trackpoints
        count = len(trackpoints)
        print('{} trackpoints loaded from file {}'.format(count, infile))
        for t in trackpoints:
            print(repr(t))
        print('---')
        print(repr(trackpoints[-1]))
        print('{} trackpoints loaded from file {}'.format(count, infile))

    if True:
        infile = 'data/activity_4564516081.tcx'
        handler = ggps.TcxHandler()
        handler.parse(infile)
        trackpoints = handler.trackpoints
        count = len(trackpoints)
        print('{} trackpoints loaded from file {}'.format(count, infile))
        for t in trackpoints:
            print(repr(t))
        print('trackpoint count: {}'.format(len(trackpoints)))

    if False:
        infile = 'data/activity_4564516081.gpx'
        handler = ggps.GpxHandler()
        handler.parse(infile)
        trackpoints = handler.trackpoints
        count = len(trackpoints)
        print('{} trackpoints loaded from file {}'.format(count, infile))
        for t in trackpoints:
            print(repr(t))

    print('version {}'.format(ggps.VERSION))
    print(str(inspect.ismodule(ggps)))

