
import json
import xml.sax

from collections import defaultdict

from ggps.base_handler import BaseHandler


class PathHandler(BaseHandler):

    @classmethod
    def parse(cls, filename):
        handler = PathHandler()
        xml.sax.parse(open(filename), handler)
        return handler

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


if __name__ == "__main__":  # pragma: no cover
    import sys
    import ggps
    handler = ggps.PathHandler.parse(sys.argv[1])
    print(handler)
