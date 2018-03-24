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
            
            for neighbour in self[node].keys():
                _next = list(path)
                _next.append(neighbour)
                queue.append(_next)
                visited.append(node)
        
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