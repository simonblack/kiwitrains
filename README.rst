Kiwitrains
==========

Kiwiland Railroad Transit library for the querying and manipulation of train route data. For use and development at Kiwiland Railroads.

Example
-------

.. code-block:: python
   
   from kiwitrains.lib import TransitMap
   data = "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
   transit_map = TransitMap(data)

   # Find the distance of the trip A-B-C.
   transit_map.trip_distance(['A','B','C'])
   9

   # Trips that do not exist return 'NO SUCH ROUTE'
   transit_map.trip_distance(['A','E','D'])
   'NO SUCH ROUTE'

   # The length of the shortest trip from B to B.
   transit_map.shortest_trip('B', 'B')
   9

   # Get the number of trips starting at C and ending at C with a maximum of 3 stops.
   transit_map.count_trips_by_stops('C', 'C', max_stops=3)
   2

   # The number of different trips from C to C with a distance less than 30.
   transit_map.count_trips_by_distance('C', 'C', max_length=30)
   7


Installation
------------

.. code-block:: bash

   $ git clone git://github.com/simonblack/kiwitrains
   $ cd kiwitrains
   $ python setup.py install


Tests
-----

.. code-block:: bash

   $ python -m kiwitrains.test
   ......
   ----------------------------------------------------------------------
   Ran 6 tests in 0.002s

   OK