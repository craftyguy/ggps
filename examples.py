
import json

import ggps

def file_types():
    return ['gpx', 'tcx']

def data_files():
    files = list()
    files.append('dav_track_5k')
    files.append('new_river_50k')
    files.append('twin_cities_marathon')
    return files

def as_json_serializable(trackpoints_list):
    json_obj = dict()
    json_obj['trackpoints'] = list()
    for t in trackpoints_list:
        json_obj['trackpoints'].append(t.values)
    return json_obj

if __name__ == "__main__":

    for base_name in data_files():
        for file_type in file_types():
            infile = "data/{0}.{1}".format(base_name, file_type)
            outfile = "data/paths/{0}_{1}.json".format(base_name, file_type)
            handler = ggps.PathHandler()
            handler.parse(infile)
            with open(outfile, 'wt') as f:
                f.write((str(handler)))
                print("PathHandler {0} -> {1}".format(infile, outfile))

    for base_name in data_files():
        for file_type in file_types():
            infile = "data/{0}.{1}".format(base_name, file_type)
            outfile = "data/parsed/{0}_{1}.json".format(base_name, file_type)
            if file_type == 'gpx':
                handler = ggps.GpxHandler()
                handler.parse(infile)
            else:
                handler = ggps.TcxHandler()
                handler.parse(infile)
            json_obj = as_json_serializable(handler.trackpoints)
            with open(outfile, 'wt') as f:
                json_str = json.dumps(json_obj, sort_keys=True, indent=2)
                f.write(json_str)
                print("GpxHandler {0} -> {1}".format(infile, outfile))
