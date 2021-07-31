# Adjacency Matrix Representation of Graph

"""     
    Space Complexity: O(n^2)
    we can check if an edge exist from point i to j in constant time
    traversing the whole graph will take O(|V|^2) time

    to construct the whole graph we only need to traverse half triangle of the matrix
"""

class Graph:
    def __init__(self, noOfVertices):
        self.totalVirtices = noOfVertices
        self.graph = [ [0] * self.totalVirtices for _ in range(self.totalVirtices) ]  # initial matrix with all values set to zero

    def addEdge(self, start, end):
        """add a single edge"""
        self.graph[start][end] = 1  # add edge by changing the value to 1
    
    def addEdges(self, edges):
        """add multiple edges"""
        for start, end in edges:
            self.addEdge(start, end)

    def printMatrix(self):
        """print the adjacency matrix of the graph"""
        print("Adjacency Matrix: ")
        for row in self.graph:
            for column in row:
                print(column, end = ' ')
            print()  # nextline      


# driver code
g = Graph(5)

edges = [
    (0, 1),
    (0, 3),
    (1, 0),
    (1, 3),
    (1, 2),
    (3, 1),
    (3, 0),
    (2, 1),
    (2, 3),
    (2, 4),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 4),
    (4, 2),
    (4, 3)
]

g.addEdges(edges)

g.printMatrix()


# Adjacency Matrix: 
# 0 1 0 1 0 
# 1 0 1 1 0 
# 0 1 0 1 1 
# 1 1 1 0 1 
# 0 0 1 1 0 