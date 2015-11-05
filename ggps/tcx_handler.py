__author__ = 'cjoakim'

import json
import sys
import xml.sax

from collections import defaultdict

from ggps.trackpoint import Trackpoint


class TcxHandler(xml.sax.ContentHandler):

    tkpt_path = "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint"

    @classmethod
    def parse(cls, filename):
        handler = TcxHandler()
        none_result =  xml.sax.parse(open(filename), handler)
        return handler

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.heirarchy = list()
        self.trackpoints = list()
        self.curr_tkpt = Trackpoint()
        self.current_text = ''

    def startElement(self, name, attrs):
        self.heirarchy.append(name)
        self.reset_curr_text()
        path = self.current_path()

        if path == self.tkpt_path:
            self.curr_tkpt = Trackpoint()
            self.trackpoints.append(self.curr_tkpt)
            return

    def endElement(self, name):
        path = self.current_path()
        if path in self.tkpt_path:
            self.curr_tkpt.set(name, self.current_text)

        self.heirarchy.pop()
        self.reset_curr_text()

    def endDocument(self):
        pass

    def reset_curr_text(self):
        self.current_text = ''

    def characters(self, chars):
        self.current_text = self.current_text + chars

    def current_depth(self):
        return len(self.heirarchy)

    def current_path(self):
        return '|'.join(self.heirarchy)

    def trackpoint_count(self):
        return len(self.trackpoints)


if __name__ == "__main__":
    filename = sys.argv[1]
    print(filename)
    handler = TcxHandler.parse(filename)
    print("{0} trackpoints parsed".format(handler.trackpoint_count()))
    print(handler.trackpoints)


