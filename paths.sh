#!/bin/bash

source bin/activate

python ggps/path_handler.py data/twin_cities_marathon.gpx > data/paths/twin_cities_marathon_gpx.json
python ggps/path_handler.py data/twin_cities_marathon.kml > data/paths/twin_cities_marathon_kml.json
python ggps/path_handler.py data/twin_cities_marathon.tcx > data/paths/twin_cities_marathon_tcx.json

python ggps/path_handler.py data/new_river_50k.gpx > data/paths/new_river_50k_gpx.json
python ggps/path_handler.py data/new_river_50k.kml > data/paths/new_river_50k_kml.json
python ggps/path_handler.py data/new_river_50k.tcx > data/paths/new_river_50k_tcx.json

echo 'done'
