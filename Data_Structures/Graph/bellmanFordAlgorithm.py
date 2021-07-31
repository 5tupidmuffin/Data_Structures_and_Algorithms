"""
    shortest path algorithm which take O(|V| * |E|) (costly than Dijkstras)
    uses dynamic programming approach
    works with negative weight unlike Dijkstras which may or may not return correct path

    ref:
        https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
"""


# import sys """ no need to since we are using float('inf') """
# infinity = float('inf')  # just for the sake of convinience


class Graph:
    infinity = float('inf')  # just for the sake of convinience and only accessable in Graph class

    def __init__(self, vertices: int):
        self.vertices = vertices
        self.graph = []  # simple list implementation with each edge represented as [u, v, w]

    def addEdge(self, start: int, end: int, weight: int) -> None:
        """add a single edge from start to end with given weight"""
        self.graph.append([start, end, weight])

    def addEdges(self, edges: list[tuple]) -> None:
        """add multiple edges"""
        for start, end, weight in edges:
            self.addEdge(start, end, weight)

    def printList(self) -> None:
        """print the graph's all edges"""
        print("Graph: ")
        for edge in self.graph:
            print(edge)

    def bellmanFord(self, source: int) -> list:
        """returns array with shortest path from source to all other nodes"""
        dist = [Graph.infinity] * self.vertices
        dist[source] = 0

        # |V| - 1 times
        for _ in range(self.vertices - 1):
            for u, v, w in self.graph:
                if dist[u] != Graph.infinity and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        return dist


# example used in geeksforgeeks
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 4, 2),
    (1, 3, 2),
    (1, 2, 3),
    (3, 2, 5),
    (4, 3, -3)
]

g = Graph(5)
g.addEdges(edges)

g.printList()
print()
print(g.bellmanFord(0))

# print(infinity)  # results in "not defined" error

# [0, 1, -1]
# [0, 2, 4]
# [1, 4, 2]
# [1, 3, 2]
# [1, 2, 3]
# [3, 2, 5]
# [4, 3, -3]

# [0, -1, 2, -2, 1]

