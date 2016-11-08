
import xml.sax

from ggps.base_handler import BaseHandler
from ggps.trackpoint import Trackpoint


class GpxHandler(BaseHandler):

    tkpt_path = "gpx|trk|trkseg|trkpt"  # ggps_src
    tkpt_path_len = len(tkpt_path)

    def parse(self, filename):
        xml.sax.parse(open(filename), self)
        return self

    def __init__(self):
        BaseHandler.__init__(self)

    def startElement(self, tag_name, attrs):
        self.heirarchy.append(tag_name)
        self.reset_curr_text()
        path = self.curr_path()

        if path == self.tkpt_path:
            self.curr_tkpt = Trackpoint()
            lat, lon = attrs['lat'],  attrs['lon']
            self.curr_tkpt.set('latitudedegrees', lat)
            self.curr_tkpt.set('longitudedegrees', lon)
            self.trackpoints.append(self.curr_tkpt)
            return

    def endElement(self, tag_name):
        path = self.curr_path()

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
                    self.curr_tkpt.set(tag_name, self.curr_text)

        self.heirarchy.pop()
        self.reset_curr_text()

    def endDocument(self):
        self.end_reached = True
        for idx, t in enumerate(self.trackpoints):
            if idx == 0:
                self.set_first_trackpoint(t)

            t.set('seq', "{0}".format(idx + 1))
            self.calculate_elapsed_time(t)
