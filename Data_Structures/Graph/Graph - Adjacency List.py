# Adjacency List Representation of Graph
"""
    Ref:
        https://www.programiz.com/dsa/graph-adjacency-list
        https://www.youtube.com/watch?v=5hPfm_uqXmw

    Space Complexity: O(|V| + 2|E|)  // 2E because we are adding a single edge twice in the list
    Checking if edge exist between i, j will require (|V|) if its the last edge because we would explore all the between nodes
"""

# for linkedList Implementation
class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:
    def __init__(self, numOfVertices):
        self.totalVertices = numOfVertices
        self.graph = [None] * self.totalVertices

    def addEdge(self, start, end):
        # requires constant time
        # makes a single edge at a time
        if self.graph[start]:
            node = Node(end)
            node.next = self.graph[start]
            self.graph[start] = node

        else:
            self.graph[start] = Node(end)

        # from programiz -
        # makes 2 edges at a time eg. ij and ji
        # node = Node(end)
        # node.next = self.graph[start]
        # self.graph[start] = node

        # node = Node(start)
        # node.next = self.graph[end]
        # self.graph[end] = node

        # what i thought first -
        # requires O(|V|) in worst case
        # if self.graph[start]:
        #     temp = self.graph[start]
        #     while temp.next:
        #         temp = temp.next
        #     temp.next = Node(end)

    def addEdges(self, edges):
        # add multiple edges
        for start, end in edges:
            self.addEdge(start, end)

    def printList(self):
        print("Adjacency List: ")
        # for i in range(self.totalVertices):
        #     print(f"Vertex {i} is connected to : ")
        #     temp = self.graph[i]
        #     while temp:
        #         print(temp.vertex, end = " ")
        #         temp = temp.next
        #     print()
        
        currentVertex = 0  # for representational purpose
        for vertex in self.graph:
            temp = vertex
            print(f"{currentVertex} :", end = "")
            while temp:
                print(temp.vertex, end = "-> ")
                temp = temp.next
            print()
            currentVertex += 1


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

g.printList()

# Adjacency List: 
# 0 :3-> 1-> 
# 1 :2-> 3-> 0-> 
# 2 :4-> 3-> 1-> 
# 3 :4-> 2-> 1-> 0-> 
# 4 :3-> 2-> 
