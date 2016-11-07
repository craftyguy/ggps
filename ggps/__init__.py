__author__ = 'cjoakim'
__version__ = '0.1.11'

"""
ggps library
"""

VERSION = __version__

import json
import m26
import xml.sax

from collections import defaultdict


class Trackpoint(object):

    def __init__(self):
        self.values = dict()
        self.values['type'] = 'Trackpoint'

    def get(self, key, default_value=''):
        if key in self.values:
            return self.values[key]
        else:
            return default_value

    def set(self, key, value):
        if key and value:
            self.values[key.lower().strip()] = value.strip()

    def __str__(self):
        template = "<Trackpoint values count:{0}>"
        return template.format(len(self.values))

    def __repr__(self):
        return json.dumps(self.values, sort_keys=True, indent=2)


class BaseHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.heirarchy = list()
        self.trackpoints = list()
        self.curr_tkpt = Trackpoint()
        self.curr_text = ''
        self.end_reached = False
        self.first_time = None
        self.first_etime = None
        self.first_time_secs_to_midnight = 0

    def endDocument(self):
        self.completed = True

    def characters(self, chars):
        if self.curr_text:
            self.curr_text = self.curr_text + chars
        else:
            self.curr_text = chars

    def reset_curr_text(self):
        self.curr_text = ''

    def curr_depth(self):
        return len(self.heirarchy)

    def curr_path(self):
        return '|'.join(self.heirarchy)

    def trackpoint_count(self):
        return len(self.trackpoints)

    def set_first_trackpoint(self, t):
        self.first_time = t.get('time')
        self.first_hhmmss = self.parse_hhmmss(self.first_time)
        self.first_etime = m26.ElapsedTime(self.first_hhmmss)
        self.first_time_secs = self.first_etime.secs

        # deal with the possibility that the Activity spans two calendar days.
        secs = int(m26.Constants.seconds_per_hour() * 24)
        self.first_time_secs_to_midnight = secs - self.first_time_secs
        if False:
            print("first_time:   {0}".format(self.first_time))
            print("first_hhmmss: {0}".format(self.first_hhmmss))
            print("first_etime:  {0}".format(self.first_etime))
            print("first_time_secs: {0}".format(self.first_time_secs))
            print("first_time_secs_to_midnight: {0} {1}".format(
                self.first_time_secs_to_midnight, secs))

    def meters_to_feet(self, t, meters_key, new_key):
        m = t.get(meters_key)
        km = float(m) / 1000.0
        d_km = m26.Distance(km, m26.Constants.uom_kilometers())
        yds = d_km.as_yards()
        t.set(new_key, str(yds * 3.000000))

    def meters_to_km(self, t, meters_key, new_key):
        m = t.get(meters_key)
        km = float(m) / 1000.0
        t.set(new_key, str(km))

    def meters_to_miles(self, t, meters_key, new_key):
        m = t.get(meters_key)
        km = float(m) / 1000.0
        d_km = m26.Distance(km, m26.Constants.uom_kilometers())
        t.set(new_key, str(d_km.as_miles()))

    def runcadence_x2(self, t):
        c = t.get('runcadence', 0)
        i = int(c)
        t.set('runcadencex2', str(i * 2))

    def calculate_elapsed_time(self, t):
        time_str = t.get('time')
        new_key = 'elapsedtime'
        if time_str:
            if time_str == self.first_time:
                t.set(new_key, '00:00:00')
            else:
                curr_time = self.parse_hhmmss(time_str)
                curr_etime = m26.ElapsedTime(curr_time.strip())
                secs_diff = curr_etime.secs - self.first_time_secs
                if secs_diff < 0:
                    secs_diff = secs_diff + self.first_time_secs_to_midnight
                elapsed = m26.ElapsedTime(secs_diff)
                t.set(new_key, elapsed.as_hhmmss())

    def parse_hhmmss(self, time_str):
        """
        For a given datetime value like '2014-10-05T17:22:17.000Z' return the
        hhmmss value '17:22:17'.
        """
        if len(time_str) > 0:
            if 'T' in time_str:
                return str(time_str.split('T')[1][:8])
            else:
                return ''
        else:
            return ''


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


class TcxHandler(BaseHandler):

    root_tag = 'TrainingCenterDatabase'
    tkpt_path = root_tag + "|Activities|Activity|Lap|Track|Trackpoint"
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
            self.trackpoints.append(self.curr_tkpt)
            return

    def endElement(self, tag_name):
        path = self.curr_path()

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
                    self.curr_tkpt.set(tag_name, self.curr_text)

        self.heirarchy.pop()
        self.reset_curr_text()

    def endDocument(self):
        self.end_reached = True
        for idx, t in enumerate(self.trackpoints):
            if idx == 0:
                self.set_first_trackpoint(t)

            t.set('seq', "{0}".format(idx + 1))
            self.meters_to_feet(t, 'altitudemeters', 'altitudefeet')
            self.meters_to_miles(t, 'distancemeters', 'distancemiles')
            self.meters_to_km(t, 'distancemeters', 'distancekilometers')
            self.runcadence_x2(t)
            self.calculate_elapsed_time(t)


class PathHandler(BaseHandler):

    def parse(self, filename):
        xml.sax.parse(open(filename), self)
        return self

    def __init__(self):
        BaseHandler.__init__(self)
        self.path_counter = defaultdict(int)

    def startElement(self, name, attrs):
        self.heirarchy.append(name)
        path = self.curr_path()
        self.path_counter[path] += 1

        for aname in attrs.getNames():
            self.path_counter[path + '@' + aname] += 1

    def endElement(self, name):
        self.heirarchy.pop()

    def curr_path(self):
        return '|'.join(self.heirarchy)

    def __str__(self):
        return json.dumps(self.path_counter, sort_keys=True, indent=2)


# built on 2016-11-07 17:11:10.667246
