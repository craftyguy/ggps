__author__ = 'cjoakim'

import sys
import xml.sax

from ggps.trackpoint import Trackpoint


class TcxHandler(xml.sax.ContentHandler):

    tkpt_path = "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint"
    tkpt_path_len = len(tkpt_path)

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

    def startElement(self, tag_name, attrs):
        self.heirarchy.append(tag_name)
        self.reset_curr_text()
        path = self.current_path()

        if path == self.tkpt_path:
            self.curr_tkpt = Trackpoint()
            self.trackpoints.append(self.curr_tkpt)
            return

    def endElement(self, tag_name):
        path = self.current_path()

        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|AltitudeMeters": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|DistanceMeters": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions|TPX": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions|TPX@xmlns": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions|TPX|RunCadence": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions|TPX|Speed": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|HeartRateBpm": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|HeartRateBpm|Value": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Position": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Position|LatitudeDegrees": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Position|LongitudeDegrees": 2256,
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Time": 2256,

        if self.tkpt_path in path:
            if len(path) > self.tkpt_path_len:
                retain = True
                if tag_name == 'Extensions':
                    retain = False
                elif tag_name == 'Position':
                    retain = False
                elif tag_name == 'TPX':
                    retain = False
                elif tag_name == 'HeartRateBpm':
                    retain = False
                elif tag_name == 'Value':
                    tag_name = 'HeartRateBpm'

                if retain:
                    self.curr_tkpt.set(tag_name, self.current_text)

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
    for t in handler.trackpoints:
        print(repr(t))


