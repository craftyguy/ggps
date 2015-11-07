
import sys
import xml.sax

from ggps.sax import BaseHandler
from ggps.trackpoint import Trackpoint


class TcxHandler(BaseHandler):

    tkpt_path = "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint"
    tkpt_path_len = len(tkpt_path)

    @classmethod
    def parse(cls, filename, augment=False):
        handler = TcxHandler(augment)
        none_result =  xml.sax.parse(open(filename), handler)
        return handler

    def __init__(self, augment=False):
        BaseHandler.__init__(self, augment)

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

        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|AltitudeMeters": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|DistanceMeters": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions|TPX": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions|TPX@xmlns": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions|TPX|RunCadence": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Extensions|TPX|Speed": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|HeartRateBpm": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|HeartRateBpm|Value": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Position": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Position|LatitudeDegrees": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Position|LongitudeDegrees": 
        # "TrainingCenterDatabase|Activities|Activity|Lap|Track|Trackpoint|Time": 

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
                if idx == 0:
                    self.set_first_trackpoint(t)
                self.augment_with_calculations(idx, t)

    def augment_with_calculations(self, idx, t):
        t.set('seq', "{0}".format(idx + 1))
        self.meters_to_feet(t, 'altitudemeters', 'altitudefeet')
        self.meters_to_miles(t, 'distancemeters', 'distancemiles')
        self.meters_to_km(t, 'distancemeters', 'distancekilometers')
        self.runcadence_x2(t)
        self.calculate_elapsed_time(t)


# python ggps/tcx_handler.py data/twin_cities_marathon.tcx

if __name__ == "__main__":
    filename = sys.argv[1]
    handler = TcxHandler.parse(filename, True)
    for t in handler.trackpoints:
        print(repr(t))
