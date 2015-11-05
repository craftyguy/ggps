__author__ = 'cjoakim'

import sys
import xml.sax

import m26

from ggps.trackpoint import Trackpoint


class TcxHandler(xml.sax.ContentHandler):

    tkpt_path = "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint"
    tkpt_path_len = len(tkpt_path)

    @classmethod
    def parse(cls, filename, augment=False):
        handler = TcxHandler(augment)
        none_result =  xml.sax.parse(open(filename), handler)
        return handler

    def __init__(self, augment=False):
        xml.sax.ContentHandler.__init__(self)
        self.augment = augment
        self.heirarchy = list()
        self.trackpoints = list()
        self.curr_tkpt = Trackpoint()
        self.current_text = ''
        self.end_reached = False

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
        self.end_reached = True

        if self.augment:
            for idx, t in enumerate(self.trackpoints):
                self.augment_with_calculations(idx, t)

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

    def augment_with_calculations(self, idx, t):
        t.set('seq', "{0}".format(idx + 1))
        self.meters_to_feet(t, 'altitudemeters', 'altitudefeet')
        self.meters_to_miles(t, 'distancemeters', 'distancemiles')

    def meters_to_feet(self, t, meters_key, new_key):
        m = t.get(meters_key)
        if m:
            km = float(m) / 1000.0
            d_km = m26.Distance(km, m26.Constants.uom_kilometers())
            yds = d_km.as_yards()
            t.set(new_key, str(yds * 3.000000))

    def meters_to_miles(self, t, meters_key, new_key):
        m = t.get(meters_key)
        if m:
            km = float(m) / 1000.0
            d_km = m26.Distance(km, m26.Constants.uom_kilometers())
            t.set(new_key, str(d_km.as_miles()))


if __name__ == "__main__":
    filename = sys.argv[1]
    print(filename)
    handler = TcxHandler.parse(filename, True)
    print("{0} trackpoints parsed".format(handler.trackpoint_count()))
    for t in handler.trackpoints:
        print(repr(t))
