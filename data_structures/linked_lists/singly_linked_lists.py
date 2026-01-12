"""
Singly Linked Lists


----- Operations -----
* Display
* Check if empty
* Get length
* Traverse list
* Lookup a value
* Modify a value
* Get head

* Insertion:
	- Insert at beginning
	- Insert at end
	- Insert at position
* Deletion:
	- Delete at beginning
	- Delete at end
	- Delete at position
"""


class SinglyNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next
  
	def __str__(self):
		return f'{self.val}'



class SinglyLinkedList:
	def __init__(self, head=None):
		self.head = head

	def display(self):
		"""Display all node values in a clean format"""
		curr = self.head
		vals = []
		while curr:
			vals.append(str(curr.val))
			curr = curr.next
		print(" -> ".join(vals))

	def is_empty(self):
		"""Check if empty"""
		return self.head is None

	def get_head(self):
		"""Return value of list head"""
		return self.head.val

	def length(self):
		"""Get length"""
		curr = self.head
		length = 0
		while curr:
			length += 1
			curr = curr.next
		return length

	def traverse(self):
		"""Traverse and print all values 1 by 1"""
		curr = self.head
		while curr:
			print(curr.val)
			curr = curr.next

	def lookup_value(self, target):
		"""Check if a target value exists in the list"""
		curr = self.head
		while curr:
			if curr.val == target:
				return True
			curr = curr.next
		return False

	def modify_value(self, index, new_val):
		"""Modify the value of a node at the specified position (assuming 0-based)"""
		if self.is_empty() or index >= self.length():
			raise IndexError("Index out of bounds")
		else:
			curr = self.head
			for i in range(self.length()):
				if i == index:
					curr.val = new_val
				curr = curr.next

	def insert_at_beginning(self, node):
		"""Insert at beginning"""
		node.next = self.head
		self.head = node

	def insert_at_pos(self, pos, node):
		"""Insert a node at a specified position (assuming 0-based)
		Requires traversing the list"""
		if pos > self.length():
			raise Exception('Position is invalid')
		curr = self.head
		i = 0
		while curr.next:
			if i == pos-1:
				node.next = curr.next  # Make the new node point to the next position
				curr.next = node  # Update the current node to point to the new node
			curr = curr.next
			i += 1

	def insert_at_end(self, node):
		"""Insert at end
		Modifying the end of a SLL requires traversing the entire list"""
		# Traverse until last node (with node.next == None) is reached
		curr = self.head
		while curr.next:
			curr = curr.next
		# Insert new node
		curr.next = node
		node.next = None
  
	def del_at_beginning(self):
		"""Delete at beginning"""
		old_head = self.head
		self.head = self.head.next
		del old_head

	def del_at_pos(self, pos):
		"""Delete a node at a specified position (assuming 0-based)
		Requires traversing the list"""
		curr = self.head
		i = 0
		while curr.next:
			if i == pos-1:
				del_node = curr.next  # Store the current node, to del later
				curr.next = curr.next.next  # Move the current node over
				del del_node
			curr = curr.next
			i += 1
   
	def del_at_end(self):
		"""Delete the last node
		Modifying the end of a SLL requires traversing the entire list"""
		# Traverse until we reach the second to last node (node.next.next == None)
		curr = self.head
		while curr.next.next:
			curr = curr.next
		del curr.next  # Delete the last node
		curr.next = None  # Update the new 'last node' to have next=None
		



A = SinglyNode(4)
sll = SinglyLinkedList(head=A)

print('\n-----------Insertion & Deletion-----------')
print('~~ Current list ~~')
sll.display()
print(f'Head: {sll.get_head()}')

print('\nA. Insert 1, 3 at beginning - O(1):')
sll.insert_at_beginning(SinglyNode(3))
sll.insert_at_beginning(SinglyNode(1))
sll.display()
print(f'Head: {sll.get_head()}')

print('\nB: Insert node with val=2 at pos 1 - O(n):')
sll.insert_at_pos(pos=1, node=SinglyNode(2))
sll.display()
print(f'Head: {sll.get_head()}')

print('\nC: Insert 5, 6 at end - O(n):')
sll.insert_at_end(SinglyNode(5))
sll.insert_at_end(SinglyNode(6))
sll.display()
print(f'Head: {sll.get_head()}')

print('\nD. Del at beginning - O(1):')
sll.del_at_beginning()
sll.display()
print(f'Head: {sll.get_head()}')

print(f'\nE: Del at end - O(n):')
sll.del_at_end()
sll.display()
print(f'Head: {sll.get_head()}')

print('\nF: Del node at pos 1 - O(n):')
sll.del_at_pos(pos=1)
sll.display()
print(f'Head: {sll.get_head()}')



print('\n\n-----------Operations-----------')
print('~~ Current list ~~')
sll.display()

print('\nTraverse list:')
sll.traverse()

print('\nList length: ', sll.length())
print('List is empty: ', sll.is_empty())

print('\nLookup 2 (int): ', sll.lookup_value(2))
print('Lookup 13 (int): ', sll.lookup_value(13))

print('\nModify value at index 1 to 100:')
sll.display()
sll.modify_value(index=1, new_val=100)
sll.display()
