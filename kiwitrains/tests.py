#!/usr/bin/env python3
"""
    Unit tests for the Kiwitrains library.

"""

import unittest
from .lib import TransitMap

TEST_DATA = "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"

class TransitMapTests(unittest.TestCase):

    def setUp(self):
        self.tmap = TransitMap(TEST_DATA)

    def test_distance_calculation(self):

        tests = [
            (('A','B','C'), 9),
            (('A','D'), 5),
            (('A','D','C'), 13),
            (('A','E','B','C','D'), 22),
            (('A','E','D'), 'NO SUCH ROUTE')
        ]
        for test in tests:
            self.assertEqual(self.tmap.trip_distance(test[0]), test[1])

    def test_shortest_trip(self):
        tests = [
            ('A','C'),
            ('B','B')
        ]
        for test in tests:
            self.assertEqual(self.tmap.shortest_trip(test[0], test[1]), 9)

    def test_trips_by_stop(self):
        test1 = [
            ['C','D','C'],
            ['C','E','B','C']
        ]
        test2 = [
            ['A', 'B', 'C', 'D', 'C'],
            ['A', 'D', 'C', 'D', 'C'],
            ['A', 'D', 'E', 'B', 'C']
        ]
        
        self.assertEqual(
            self.tmap.find_trips_by_stops('C','C', max_stops=3),
            test1
        )
        self.assertEqual(
            self.tmap.find_trips_by_stops('A','C' ,min_stops=4, max_stops=4),
            test2
        )

    def test_trips_by_distance(self):
        test = [
            ['C', 'D', 'C'], 
            ['C', 'E', 'B', 'C'],
            ['C', 'D', 'E', 'B', 'C'], 
            ['C', 'D', 'C', 'E', 'B', 'C'], 
            ['C', 'E', 'B', 'C', 'D', 'C'], 
            ['C', 'E', 'B', 'C', 'E', 'B', 'C'], 
            ['C', 'E', 'B', 'C', 'E', 'B', 'C', 'E', 'B', 'C']
        ]
        self.assertEqual(
            self.tmap.find_trips_by_distance('C', 'C', max_length=30),
            test
        )

    def test_count_trips_by_stop(self):
        self.assertEqual(
            self.tmap.count_trips_by_stops('C','C', max_stops=3),
            2
        )
        self.assertEqual(
            self.tmap.count_trips_by_stops('A','C' ,min_stops=4, max_stops=4),
            3
        )

    def test_count_trips_by_distance(self):
        self.assertEqual(
            self.tmap.count_trips_by_distance('C', 'C', max_length=30), 7)


if __name__ == '__main__':
    unittest.main()