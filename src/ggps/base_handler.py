
import xml.sax

import m26

from ggps.trackpoint import Trackpoint


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
