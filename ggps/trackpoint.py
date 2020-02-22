
import json


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
            if ':' in key:
                ns_removed_tagname = key.split(':')[1]
                self.values[ns_removed_tagname.lower().strip()] = value.strip()
            else:
                self.values[key.lower().strip()] = value.strip()

    def __str__(self):
        template = "<Trackpoint values count:{0}>"
        return template.format(len(self.values))

    def __repr__(self):
        return json.dumps(self.values, sort_keys=True, indent=2)
