from short_path import short_path

class Node:
    def __init__(self, name):
        self.name = name
        self.out_edges = []

    def add_edge(self, edge):
        self.out_edges.append(edge)

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.name == other.name
        return False

class Edge:
    def __init__(self, tail, head, weight):
        self.tail = tail
        self.head = head
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

# Create nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

# Create edges with weights
AB = Edge(A, B, 1)
AC = Edge(A, C, 3)
BC = Edge(B, C, 1)
BD = Edge(B, D, 4)
CD = Edge(C, D, 1)
CE = Edge(C, E, 2)
DE = Edge(D, E, 1)

A.add_edge(AB)
A.add_edge(AC)
B.add_edge(BC)
B.add_edge(BD)
C.add_edge(CD)
C.add_edge(CE)
D.add_edge(DE)

# Find the shortest path from A to E
shortest_path, shortest_weight = short_path(A, E, lambda edge: edge.weight)

# Print the result
print("Shortest path:", "->".join(node.name for edge in shortest_path for node in (edge.tail, edge.head)))
print("Shortest weight:", shortest_weight)
