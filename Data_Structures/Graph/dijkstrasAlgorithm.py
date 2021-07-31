"""
    Dijkstra's Algorithm finds shortest path from source to every other node.
    for this it uses greedy approach therefore its not the best approach
    
    ref:
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        https://www.youtube.com/watch?v=XB4MIexjvY0
        https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

    time complexity: O(|V|^2) 
"""
import sys

class Graph:
    """
        Adjacency Matrix Representation
        Undirected Graph
    """
    def __init__(self, vertices):
        self.totalVertices = vertices
        self.graph = [ [0] * self.totalVertices for x in range(self.totalVertices) ]  # Adjacency Matrix

    def printMatrix(self):
        """print the adjacency matrix"""
        for row in self.graph:
            for column in row:
                print(column, end=" ")
            print()


    def addEdge(self, start, end, weight):
        """add edge with given weight"""
        self.graph[start][end] = weight
        self.graph[end][start] = weight

    def addEdges(self, edges):
        """add multiples edges"""
        for start, end, weight in edges:
            self.addEdge(start, end, weight)

    def minDistance(self, distArray, visitedarray):
        min_distance = sys.maxsize
        min_vertex = -1

        for vertex in range(self.totalVertices):
            if distArray[vertex] < min_distance and visitedarray[vertex] == False:
                min_distance = distArray[vertex]
                min_vertex = vertex

        return min_vertex

    def Dijkstra(self, source):
        """
            Dijksta's Algorithm for shortest path from given source node to every other
            it only finds the path values not the actual path
        """
        visited = [False] * self.totalVertices
        distance = [sys.maxsize] * self.totalVertices
        distance[source] = 0  # distance from source to source will be zero

        for _ in range(self.totalVertices):
            u = self.minDistance(distance, visited)
            visited[u] = True

            for v in range(self.totalVertices):
                if self.graph[u][v] > 0 and visited[v] == False and distance[v] > distance[u] + self.graph[u][v]:
                    distance[v] = distance[u] + self.graph[u][v]

        return distance


edges = [
    (0, 1, 4),
    (0, 2, 4),
    (1, 2, 2),
    (2, 3, 3),
    (2, 4, 1),
    (2, 5, 6),
    (3, 5, 2),
    (4, 5, 3)
]

# example from geeksforgeeks
edges2 = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 2, 8),
    (1, 7, 11),
    (2, 8, 2),
    (2, 5, 4),
    (2, 3, 7),
    (3, 4, 9),
    (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 8, 6),
    (6, 7, 1),
    (7, 8, 7)
]

g = Graph(6)
g.addEdges(edges)
g.printMatrix()
print(g.Dijkstra(0))

# 0 4 4 0 0 0 
# 4 0 2 0 0 0
# 4 2 0 3 1 6
# 0 0 3 0 0 2
# 0 0 1 0 0 3
# 0 0 6 2 3 0
# [0, 4, 4, 7, 5, 8]

