
import json


class Trackpoint(object):

    def __init__(self):
        self.values = dict()
        self.values['type'] = 'Trackpoint'

    def get(self, key):
        return self.values[key]

    def set(self, key, value):
        if key:
            self.values[key.lower().strip()] = value.strip()

    def __str__(self):
        template = "<Trackpoint values count:{0}>"
        return template.format(len(self.values))

    def __repr__(self):
        return json.dumps(self.values, sort_keys=True, indent=2)
