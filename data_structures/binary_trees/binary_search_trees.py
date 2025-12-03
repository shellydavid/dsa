"""
Binary Search Trees

BSTs are Binary Trees with the following special properties:
	- All descendants to the LEFT of a node are <
	- All descendants to the RIGHT of a node are >=

This make searching a value very efficient: O(log n)
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
#             5(A)
#      1(B)         8(C)
#  -1(D)  3(E)   7(F)  9(G)
"""

A = TreeNode(5)
B = TreeNode(1)
C = TreeNode(8)
D = TreeNode(-1)
E = TreeNode(3)
F = TreeNode(7)
G = TreeNode(9)

A.left, A.right = B, C
B.left, B.right = D, E
C.left, C.right = F, G


# Doing a DFS inorder traversal on a BST will print the elements in sorted order
def dfs_inorder(node):
	if node is None:
		return
	dfs_inorder(node.left)
	print(node)
	dfs_inorder(node.right)

print('\nDFS inorder on BST:')
dfs_inorder(A)


# Searching for a Value
# 	Time: O(log n)
# 	Space: O(n)
def bst_search(node, target):
	if node is None:
		return False
	elif node.val == target:
		return True
	elif target < node.val:
		return bst_search(node.left, target)
	else:
		return bst_search(node.right, target)

print('\nBST search:')
print(bst_search(A, 5))
print(bst_search(A, 3))
print(bst_search(A, 7))
print(bst_search(A, 8))
print(bst_search(A, 20))
print(bst_search(A, 15))
