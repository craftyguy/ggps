__author__ = 'cjoakim'

import xml.sax

# python cj/xml/parsing.py > data/postal_codes_nc.csv


import json

from collections import defaultdict


class PathHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.heirarchy = list()
        self.path_counter = defaultdict(int)

    def startElement(self, name, attrs):
        self.heirarchy.append(name)
        path = self.current_path()
        self.path_counter[path] += 1

        for aname in attrs.getNames():
            self.path_counter[path + '@' + aname] += 1

    def endElement(self, name):
        self.heirarchy.pop()

    def endDocument(self):
        json_str = json.dumps(self.path_counter, sort_keys=True, indent=2)
        print(json_str)

    def characters(self, content):
        pass
        #self.current_value.append(content)

    def current_path(self):
        return '|'.join(self.heirarchy)


def main(sourceFileName):
    source = open(sourceFileName)
    xml.sax.parse(source, PathHandler())

if __name__ == "__main__":
    filename = "data/activity_930994230.kml"
    filename = "data/activity_893959925.kml"
    main(filename)
