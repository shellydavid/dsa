"""
Graphs

Representations:
- Edge List (array of edges)
- Adjacency Matrix
- Adjacency List

Typically in Leetcode, you will be presented with an edge list and can
convert it to the more useful adjacency list

Traversals:
- DFS recursion (stack)
- DFS iterative + stack
- BFS queue

"""


""" --------- Representations & Conversions ------------------ """

# ----- Edge List/Array of Edges -----
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
n = 8  # num nodes


# ----- CONVERTING Array of Edges -> Adjacency Matrix -----
# Instantiate matrix of 0s with the proper size
M = []
for i in range(n):
	M.append([0]*n)

for u, v in A:
	M[u][v] = 1
	# For an undirected graph, add the following:
	# M[v][u] = 1

print('Adjacency matrix: ', M)


# ----- CONVERTING Array of Edges -> Adjacency List -----
from collections import defaultdict

D = defaultdict(list)  # a node with no connections should have an empty list by default

for u, v in A:
	D[u].append(v)
	# For an undirected graph, add the following:
	# D(v).append(u)

print('Adjacency list: ', D)



""" --------- Traversals ------------------ """

# ----- DFS (stack - recursive) -----
# Time: O(V+E)

source_node = 0  # Define the node to start at
seen = set()  # prevent cycles
seen.add(source_node)

def dfs_recursive(node):
	# Do your processing (in this case, just a print)
	print(node)
	# Traverse
	for conn in D[node]:
		if conn not in seen:
			seen.add(conn)
			dfs_recursive(conn)

print('\nDFS recursive')
dfs_recursive(source_node)


# ----- DFS (stack - iterative) -----
# Time: O(V+E)
source_node = 0
# Initialize seen set
seen = set()
seen.add(source_node)
# Initialize stack
stack = [source_node]

def dfs_iterative(stk):
	while stk:
		curr_node = stk.pop()
		# Processing - in this case just a print
		print(curr_node)
		for conn in D[curr_node]:
			if conn not in seen:
				seen.add(conn)
				stk.append(conn)

print('\nDFS iterative')
dfs_iterative(stack)


# ----- BFS (queue) -----
# Time: O(V+E)
from collections import deque

source_node = 0
seen = set()
seen.add(source_node)
q = deque()
q.append(source_node)

def bfs(q):
	while q:
		curr_node = q.popleft()
		# Processing
		print(curr_node)
		for conn in D[curr_node]:
			if conn not in seen:
				seen.add(conn)
				q.append(conn)

print('\nBFS')
bfs(q)



""" ----- Representing Graphs + Nodes as Classes ----- """

class Node:
	def __init__(self, val):
		self.value = val
		self.neighbors = []

	def __str__(self):
		return f"Node{self.value}"

	def display(self):
		cons = [node.value for node in self.neighbors]
		print(f"Node{self.value} is connected to {cons}")

print('\nNode as a class')
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

A.display()
B.display()
C.display()
D.display()
