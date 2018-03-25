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
        # convert csv to adjacency mapping on self
        for route in csv.split(', '):
            
            if route[0] not in self:
                self[route[0]] = {}
            
            self[route[0]][route[1]] = int(route[2])
    
    def __bfs(self, start, end, min_depth=1, max_depth=5):
        """
        Perform a breadth-first search.
        
        Args:
            start (str): The root node.
            end (str): The terminal node.
        
        Kwargs:
            min_depth (int): The minimum traversal depth. Defaults to 1.
            max_depth (int): The maximum traversal depth. Defaults to 5.
        
        Returns: 
            paths (list): A list of discovered paths.
        """
        paths = []
        visited = []
        queue = [start]
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node == end and len(queue):
                if len(path) <= max_depth:
                    if len(path) >= min_depth:
                        paths.append(path)
                else:
                    break # stop traversal if we reach length limits
            
            if node in visited:
                if len(path) > max_depth:
                    continue
            try:
                for neighbour in self[node].keys():
                    _next = list(path)
                    _next.append(neighbour)
                    queue.append(_next)
                    visited.append(node)
            except KeyError: # Inexistent node means path doesn't exist.
                return "NO SUCH ROUTE"

        return paths
    
    def __dijkstra(self, start):
        """
        Find the shortest paths relative to the root node.
        
        Args:
            start (str): The root node.
        
        Returns:
            (tuple): A tuple containing:

                visited (dict): Distances from root node to other nodes.
                chain (dict): A dict representation of the traversed path.
        """
        visited = {start:0}
        queue = set(self.keys())
        chain = {}
        
        while queue: 
            root = None
            
            for node in queue:
                if node in visited and not root:
                    root = node
            
            if root is None:
                break
            
            queue.remove(root)
            current_weight = visited[root]
            
            # Remove the root node from the visited nodes map in order to
            # find paths that start and end with the same node.
            if not visited[root]:
                del visited[root]
            
            for edge in self[root]:
                weight = self[root][edge] + current_weight
                
                if (edge not in visited or visited[edge] > weight):
                    visited[edge] = weight
                    chain[edge] = root
            
        return visited, chain
    
    def _shortest_path(self, start, end):
        """
        Find the shortest path between two nodes.
        
        Args:
            start (str): The root node.
            end (str): The terminal node.

        Returns:
            (tuple): A tuple containing:
            
                dist (int): The distance of the shortest path.
                path (list): A list containing the path of the shortest path.
        """
        visited, chain = self.__dijkstra(start)
        path = [end]
        
        try:
            dist = visited[end]
        except KeyError:
            return "NO SUCH ROUTE"
        
        # If matching a path that starts and ends with the same node,
        # process the first node outside of the loop in order to 
        # to avoid ending the loop before buiding a complete path.
        if end == start:
            end = chain[end]
            path.append(end)
        
        while end != start:
            end = chain[end]
            path.append(end)
            
        path.reverse()
    
        return dist, path
    
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
        trips = self.find_trips_by_distance(start, end, min_length, max_length)
        
        if isinstance(trips, str):
            return 0
        else:
            return len(trips)

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
        trips = self.find_trips_by_stops(start, end, min_stops, max_stops)
        
        if isinstance(trips, str):
            return 0
        else:
            return len(trips)

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
        trips = []
        paths = self.find_trips_by_stops(start,end)

        for path in paths:
            length = self.trip_distance(path)
            if min_length < length < max_length:
                trips.append(path)

        return trips

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
        # min/max search depths are equal to min/max stops + 1 because trip
        # stop counts do not include the root node
        min_depth = min_stops + 1
        max_depth = max_stops + 1
        
        trips = self.__bfs(start, end, min_depth, max_depth)
        return trips

    def shortest_trip(self, start, end):
        """
        Find the shortest trip between two stopss.
        
        Args:
            start (str): The trip origin.
            end (str): The final stop.
        
        Returns:
            (int): Length of shortest route.
        
        """
        return self._shortest_path(start,end)[0]
        
    def trip_distance(self, path):
        """
        Calculate total trip distance.

        Args:
            path (list): A list of trips.

        Returns:
            distance (int): The total trip distance.
        """
        trip = list(path)
        try:
            distance = 0
            prev = trip.pop(0)
            while trip:
                stop = trip.pop(0)
                distance += self[prev][stop]
                prev = stop
        
        except KeyError:
            return "NO SUCH ROUTE"

        return distance