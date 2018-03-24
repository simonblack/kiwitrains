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
