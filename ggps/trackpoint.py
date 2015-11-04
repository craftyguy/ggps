

class Trackpoint(object):

    def __init__(self, filename):
        self.values = dict()

    def set(self, key, value):
        if key:
            self.values[key.lower().strip()] = value
