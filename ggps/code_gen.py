__author__ = 'cjoakim'

import json
import sys

from ggps import xml_paths


class CodeGenerator(object):

    def __init__(self, filename):
        self.filename = filename
        self.determine_source_filetype()
        self.data = dict()
        self.paths = list()

    def load(self):
        try:
            with open(self.filename, 'r') as json_file:
                self.data = json.loads(json_file.read())
                pathlist = sorted(self.data.keys())
                for path in pathlist:
                    self.paths.append(path)
        except:
            print("Exception when loading file: " + self.filename)
            self.data = {}

    def determine_source_filetype(self):
        self.filetype, self.tkpt_path = '', ''

        if '_gpx' in self.filename:
            self.filetype = 'gpx'
            self.tkpt_path = xml_paths.gpx_tkpt_path()

        if '_kml' in self.filename:
            self.filetype = 'kml'

        if '_tcx' in self.filename:
            self.filetype = 'tcx'
            self.tkpt_path = xml_paths.tcx_tkpt_path()

    def generate(self):
        self.load()
        print(self.data)
        print(self.paths)
        print(self.filename)
        print(self.filetype)
        print(self.tkpt_path)

        for path in self.paths:
            if self.tkpt_path in path:
                print(path)

# python ggps/code_gen.py data/paths/twin_cities_marathon_gpx.json

if __name__ == "__main__":
    filename = sys.argv[1]
    generator = CodeGenerator(filename)
    generator.generate()
