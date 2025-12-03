"""
Binary Trees

-------- Traversal approaches --------
1. Depth First Search (DFS)
Search along the 'height' of the tree (vertically)
	- Preorder: NODE - LEFT - RIGHT
	- Inorder: LEFT - NODE - RIGHT
	- Postorder: LEFT - RIGHT - NODE

DFS can be done recursively or iteratively
DFS uses a STACK


2. Breadth First Search (BFS or Level-Order)
Search along the 'levels' of the tree (horizontally)
BFS uses a QUEUE
"""


class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.val)

"""
Tree structure:
#              1(A)
#       2(B)          3(C)
#   4(D)   5(E)   10(F)
"""

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left, A.right = B, C
B.left, B.right = D, E
C.left = F


""" DFS ----------------------------------------------------
# Preorder traversal (NLR): 1, 2, 4, 5, 3, 10
# Inorder traversal (LNR): 4, 2, 5, 1, 10, 3
# Postorder traversal (LRN): 4, 5, 2, 10, 3, 1
"""

# Recursive Pre Order Traversal (DFS)
# 	Time: O(n)
# 	Space: O(n)
def dfs_preorder(node):
	if node is None:
		return
	# N -> L -> R
	print(node)
	dfs_preorder(node.left)
	dfs_preorder(node.right)

print('(Recursive) DFS preorder:')
dfs_preorder(A)


# Recursive In Order Traversal (DFS)
# 	Time: O(n)
# 	Space: O(n)
def dfs_inorder(node):
	if node is None:
		return
	# L -> N -> R
	dfs_inorder(node.left)
	print(node)
	dfs_inorder(node.right)

print('\n(Recusrive) DFS_inorder:')
dfs_inorder(A)


# Recursive Post Order Traversal (DFS)
# 	Time: O(n)
# 	Space: O(n)
def dfs_postorder(node):
	if not node:
		return
	# L -> R -> N
	dfs_postorder(node.left)
	dfs_postorder(node.right)
	print(node)

print('\n(Recursive) DFS postorder:')
dfs_postorder(A)


# Iterative Pre Order Traversal (DFS)
# 	Time: O(n)
# 	Space: O(n)
def iter_dfs(node):
	stack = [node]
	while stack:
		# N -> L -> R
		node = stack.pop()
		# No matter how you order the print statement, it will always be preorder
		# bec appending to a stack iteratively does not force you down any recursive path
		print(node)
		# Since it's a stack, push R first, then L so L gets popped first
		if node.right: stack.append(node.right)
		if node.left: stack.append(node.left)

print('\n(Iterative) DFS preorder:')
iter_dfs(A)


# Search Value (DFS)
# 	Time: O(n)
# 	Space: O(n)
def dfs_search(node, target) -> bool:
	if node is None:
		return False

	if node.val == target:
		return True

	return dfs_search(node.left, target) or dfs_search(node.right, target)

print('\nDFS search:')
print(dfs_search(A, 2))
print(dfs_search(A, 4))
print(dfs_search(A, 20))
print(dfs_search(A, 15))


""" BFS ----------------------------------------------------
Traversal: 1, 2, 3, 4, 5, 10
"""

# BFS/Level Order Traversal
# 	Time: O(n)
# 	Space: O(n)
from collections import deque
def bfs(node):
	q = deque()
	q.append(node)

	while q:
		# Since it's a queue, push L first, then R so L gets dequeued first
		node = q.popleft()
		print(node)
		if node.left: q.append(node.left)
		if node.right: q.append(node.right)

print('\nBFS:')
bfs(A)
