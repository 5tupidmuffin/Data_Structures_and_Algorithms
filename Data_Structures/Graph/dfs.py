"""
    DFS utilizes stack instead of queue in bfs
    dfs is not complete

    for a tree dfs is same as preorder traversal

    ref:
        https://en.wikipedia.org/wiki/Depth-first_search#Pseudocode
    time complexity: O(|V| + |E|)
    space complexity: O(|V|)
    ref:
        https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
"""

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        # instead of returning key error we can use defaultdict it will return an empty list
    
    def addEdge(self, start, end):
        if start in self.graph.keys():
            self.graph[start].append(end)
        else:
            self.graph[start] = [end]

    def depthFirstTraversal_iterative(self, startVertex):
        print("Iterative DFS:", end= " ")
        visited = [False] * self.vertices
        stack = []  # LIFO

        visited[startVertex] = True
        stack.append(startVertex)

        while stack:
            current = stack.pop()
            print(current, end=" ")

            for i in self.graph[current]:
                if visited[i] == False:
                    visited[i] = True
                    stack.append(i)
        print()

    def depthFirstTraversal_recursive(self, startVertex):
        print("Recursive DFS: ", end="")
        visited = set()  # we can also use list

        self.dfs_helper(startVertex, visited)
        print()

    def dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for i in self.graph[vertex]:
            if i not in visited:
                self.dfs_helper(i, visited)



# driver code
g = Graph(5)

# Directed Graph
g.addEdge(0, 1)
g.addEdge(0, 3)

g.addEdge(1, 0)
# g.addEdge(1, 3)
g.addEdge(1, 2)

# g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(2, 4)

# g.addEdge(3, 0)
g.addEdge(3, 1)
# g.addEdge(3, 2)
g.addEdge(3, 4)

# g.addEdge(4, 2)
# g.addEdge(4, 3)

g.depthFirstTraversal_iterative(0)
g.depthFirstTraversal_recursive(0)

# Iterative DFS: 0 3 4 1 2 
# Recursive DFS: 0 1 2 3 4 

