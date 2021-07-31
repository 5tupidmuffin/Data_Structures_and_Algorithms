"""
    in BFS we travel one level at a time it uses queue[FIFO]
    to counter loops we use keep track of visited nodes with "visited" boolean array
    BFS is complete

    ref:
        https://en.wikipedia.org/wiki/Breadth-first_search
    time complexity: O(|V| + |E|) or O(V^2) if adjacency matrix is used
    space complexity: O(|V|)

    ref:
        https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
"""

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = dict()  # Adjacency List

    def addEdge(self, start, end):
        if start in self.graph.keys():
            self.graph[start].append(end)
        else:
            self.graph[start] = [end]

    def breadthfirstTravesal(self, startVertex):
        print("Breadth First Traversal: ", end= "")
        visited = [False] * self.vertices
        queue = []  # to keep track of unvisited nodes #FIFO

        visited[startVertex] = True
        queue.append(startVertex)

        while queue:
            temp = queue.pop(0)  # take the first item so as to follow FIFO
            print(temp, end=" ")
            for vertex in self.graph[temp]:
                if visited[vertex] == False:
                    queue.append(vertex)
                    visited[vertex] = True
        print()


# driver code
g = Graph(5)

g.addEdge(0, 1)
g.addEdge(0, 3)

g.addEdge(1, 0)
g.addEdge(1, 3)
g.addEdge(1, 2)

g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(2, 4)

g.addEdge(3, 0)
g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(3, 4)

g.addEdge(4, 2)
g.addEdge(4, 3)

g.breadthfirstTravesal(0)

# Breadth First Traversal: 0 1 3 2 4 

