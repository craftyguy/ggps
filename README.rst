ggps - gps file utilities for garmin connect and garmin devices
===============================================================

Features
--------

- Parse *.gpx, *.kml, and *.tcx files downloaded from Garmin Connect


Quick start
-----------

Installation:

.. code-block:: console

    $ pip install ggps

Use:

.. code-block:: pycon

    >>> import ggps

    >>> infile = 'data/new_river_50k.gpx'
    >>> augment_with_m26_calculations = True
    >>> handler = ggps.GpxHandler.parse(infile, augment_with_m26_calculations)
    >>> trackpoints = handler.trackpoints
    >>> len(trackpoints)
    2636
    >>> print(trackpoints[-1].values)

    >>> infile = 'data/twin_cities_marathon.tcx'
    >>> augment_with_m26_calculations = True
    >>> handler = ggps.TcxHandler.parse(infile, augment_with_m26_calculations)
    >>> trackpoints = handler.trackpoints
    >>> len(trackpoints)
    2222
    >>> print(trackpoints[-1].values)


Source Code
===========

See `ggps at GitHub <https://github.com/cjoakim/ggps>`_ .


Changelog
=========

Version 0.0.5
-------------

-  2015/11/07. Version 0.0.5, Alpha.
-  2015/11/01. Project created, in Alpha state.
