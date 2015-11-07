
import sys
import xml.sax

from ggps.base_handler import BaseHandler
from ggps.trackpoint import Trackpoint


class GpxHandler(BaseHandler):

    tkpt_path = "gpx|trk|trkseg|trkpt"
    tkpt_path_len = len(tkpt_path)

    @classmethod
    def parse(cls, filename, augment=False):
        handler = GpxHandler(augment)
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
            lat, lon = attrs['lat'],  attrs['lon']
            if lat:
                self.curr_tkpt.set('latitudedegrees', lat)
            if lon:
                self.curr_tkpt.set('longitudedegrees', lon)
            self.trackpoints.append(self.curr_tkpt)
            return

    def endElement(self, tag_name):
        path = self.current_path()

        # "gpx|trk|trkseg|trkpt": 2256,
        # "gpx|trk|trkseg|trkpt@lat": 2256,
        # "gpx|trk|trkseg|trkpt@lon": 2256,
        # "gpx|trk|trkseg|trkpt|ele": 2256,
        # "gpx|trk|trkseg|trkpt|extensions": 2256,
        # "gpx|trk|trkseg|trkpt|extensions|gpxtpx:TrackPointExtension": 2256,
        # "gpx|trk|trkseg|trkpt|extensions|gpxtpx:TrackPointExtension|gpxtpx:hr": 2256,
        # "gpx|trk|trkseg|trkpt|time": 2256

        if self.tkpt_path in path:
            if len(path) > self.tkpt_path_len:
                retain = True
                if tag_name == 'ele':
                    retain = False
                elif tag_name == 'extensions':
                    retain = False
                elif tag_name == 'gpxtpx:TrackPointExtension':
                    retain = False
                elif tag_name == 'gpxtpx:hr':
                    tag_name = 'heartratebpm'

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
        self.calculate_elapsed_time(t)


if __name__ == "__main__":
    filename = sys.argv[1]
    handler = GpxHandler.parse(filename, True)
    for t in handler.trackpoints:
        print(repr(t))
