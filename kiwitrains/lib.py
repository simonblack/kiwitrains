#!/usr/bin/env python3
"""
    Kiwiland Railroad Transit library.

    This module provides a TransitMap object for the querying and 
    manipulation of train route data for use at Kiwiland Railroads

"""


class TransitMap(dict):
    """
    An adjacency map-type object for interacting with train routes.
    
    Initialization data should be in the form of a comma-space-separated 
    values string of graph edges.
    Example Input: "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
    
    """
    
    def __init__(self, csv):
        # convert csv to adjacency mapping
    
    def __bfs(self, start, end, min_depth=1, max_depth=5):
        """breadth-first search.
        
        Args:
            start (str): The root node.
            end (str): The terminal node.
        
        Kwargs:
            min_depth (int): The minimum traversal depth. Defaults to 1.
            max_depth (int): The maximum traversal depth. Defaults to 5.
        
        
        """
    
    def __dijkstra(self, start):
        """
        Find the shortest paths relative to the root node.
        
        Args:
            start (str): The root node.
        
        """
    
    def count_trips_by_distance(self, start, end, min_length=0, max_length=20):
        """
        Find all trips between two stops within a specified distance.

        Args:
            start (str): The trip origin.
            end (str): The final stop.
        
        Kwargs:
            min_length (int): The minimum trip length. Defaults to 1.
            max_length (int): The maximum trip length. Defaults to 5.

        Returns:
            count (int): The total number of trips.

        """


    def count_trips_by_stops(self, start, end, min_stops=1, max_stops=10):
        """
        Find all trips between two stops.
        
        Args:
            start (str): The trip origin.
            end (str): The final stop.
        
        Kwargs:
            min_stops (int): The minimum # of stops per trip. Defaults to 2.
            max_stops (int): The maximum # of stops per trip. Defaults to 5.
        
        Returns:
            count (int): The total number of trips.
        
        """


    def find_trips_by_distance(self, start, end, min_length=0, max_length=20):
        """
        Find all trips between two stops within a specified distance.

        Args:
            start (str): The trip origin.
            end (str): The final stop.
        
        Kwargs:
            min_length (int): The minimum trip length. Defaults to 1.
            max_length (int): The maximum trip length. Defaults to 5.

        Returns:
            trips (list): A list of trips.

        """


    def find_trips_by_stops(self, start, end, min_stops=1, max_stops=10):
        """
        Find all trips between two stops.
        
        Args:
            start (str): The trip origin.
            end (str): The final stop.
        
        Kwargs:
            min_stops (int): The minimum # of stops per trip. Defaults to 2.
            max_stops (int): The maximum # of stops per trip. Defaults to 5.
        
        Returns:
            trips (list): A list of trips.
        
        """


    def shortest_trip(self, start, end):
        """
        Find the shortest trip between two stopss.
        
        """
        
    def trip_distance(self, path):
        """
        Calculate total trip distance.

        """