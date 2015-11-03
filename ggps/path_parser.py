__author__ = 'cjoakim'

import json
import sys
import xml.sax

from collections import defaultdict

from ggps import base_handler


class PathHandler(base_handler.BaseHandler):

    @classmethod
    def parse(cls, filename):
        handler = PathHandler()
        none_result =  xml.sax.parse(open(filename), handler)
        return handler

    def __init__(self):
        base_handler.BaseHandler.__init__(self)
        self.path_counter = defaultdict(int)

    def startElement(self, name, attrs):
        self.heirarchy.append(name)
        path = self.current_path()
        self.path_counter[path] += 1

        for aname in attrs.getNames():
            self.path_counter[path + '@' + aname] += 1

    def endElement(self, name):
        self.heirarchy.pop()

    def current_path(self):
        return '|'.join(self.heirarchy)

    def __str__(self):
        return json.dumps(self.path_counter, sort_keys=True, indent=2)

# python ggps/path_parser.py data/twin_cities_marathon.gpx > data/paths/twin_cities_marathon_gpx.json

if __name__ == "__main__":
    filename = sys.argv[1]
    handler = PathHandler.parse(filename)
    print(handler)
    print(handler.completed)
