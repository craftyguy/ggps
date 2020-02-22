ggps - gps file utilities for garmin connect and garmin devices
===============================================================

Features
--------

- Parse gpx and tcx files downloaded from Garmin Connect
- The GPX parsed Trackpoint data includes additional/augmented values, including as "seq" and "elapsedtime".
- The TCX parsed Trackpoint data additionally includes additional/augmented values, such as "altitudefeet", "distancemiles", "distancekilometers", and "runcadencex2".


Quick start
-----------

Installation:

.. code-block:: console

    $ pip install ggps

Use:

.. code-block:: pycon

    >>> import ggps

    >>> infile = 'data/activity_4564516081.gpx'
    >>> handler = ggps.GpxHandler()
    >>> handler.parse(infile)
    >>> trackpoints = handler.trackpoints
    >>> print(repr(trackpoints[-1]))
    {
      "cadence": "86",
      "cadencex2": "172",
      "elapsedtime": "02:51:26",
      "heartratebpm": "171",
      "latitudedegrees": "35.50814299844205379486083984375",
      "longitudedegrees": "-80.83528247661888599395751953125",
      "seq": "2177",
      "time": "2020-02-17T20:06:28.000Z",
      "trackpointextension": "",
      "type": "Trackpoint"
    }

    >>> infile = 'data/twin_cities_marathon.gpx'
    >>> handler = ggps.GpxHandler()
    >>> handler.parse(infile)
    >>> trackpoints = handler.trackpoints
    >>> len(trackpoints)
    2256

    >>> print(repr(trackpoints[-1]))
    {
      "elapsedtime": "04:14:24",
      "heartratebpm": "161",
      "latitudedegrees": "44.95180849917233",
      "longitudedegrees": "-93.10493202880025",
      "seq": "2256",
      "time": "2014-10-05T17:22:17.000Z",
      "type": "Trackpoint"
    }

    >>> infile = 'data/twin_cities_marathon.tcx'
    >>> handler = ggps.TcxHandler()
    >>> handler.parse(infile)
    >>> trackpoints = handler.trackpoints
    >>> len(trackpoints)
    2256

    >>> print(repr(trackpoints[-1]))
    {
      "altitudefeet": "864.8294163501167",
      "altitudemeters": "263.6000061035156",
      "cadence": "77",
      "cadencex2": "154",
      "distancekilometers": "42.63544921875",
      "distancemeters": "42635.44921875",
      "distancemiles": "26.492439912628992",
      "elapsedtime": "04:14:24",
      "heartratebpm": "161",
      "latitudedegrees": "44.95180849917233",
      "longitudedegrees": "-93.10493202880025",
      "seq": "2256",
      "speed": "3.5460000038146977",
      "time": "2014-10-05T17:22:17.000Z",
      "type": "Trackpoint"
    }


Source Code
===========

See `ggps at GitHub <https://github.com/cjoakim/ggps>`_ .

Includes sample data files.


Changelog
=========

Version 0.3.0
--------------

-  2020/02/22. Version 0.3.0,  Parsing improvements, normalize 'cadence' and 'heartratebpm' attribute names.
-  2020/02/19. Version 0.2.1,  Upgraded the m26 and Jinga2 libraries.
-  2017/09/27. Version 0.2.0,  Converted to the pytest testing framework.
-  2017/09/26. Version 0.1.13, packaging.
-  2016/11/07. Version 0.1.12, updated packaging.
-  2016/11/07. Version 0.1.11, updated packaging.
-  2016/11/07. Version 0.1.10, updated packaging.
-  2016/11/07. Version 0.1.9,  updated packaging.
-  2016/11/07. Version 0.1.8,  updated packaging.
-  2016/11/06. Version 0.1.7,  updated description.
-  2016/11/06. Version 0.1.6,  republished.
-  2016/11/06. Version 0.1.5,  refactored ggps/ dir.
-  2016/11/06. Version 0.1.4,  refactored ggps/ dir. nose2 for tests.
-  2015/11/07. Version 0.1.3,  Added README.rst
-  2015/11/07. Version 0.1.1   Initial release.
