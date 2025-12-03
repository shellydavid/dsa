"""
Singly Linked Lists


----- Operations -----
* Display
* Check if empty
* Get length
* Traverse list
* Lookup a value
* Modify a value
* Get head  # TODO

* Insertion:
	- Insert at beginning
	# TODO (below)
	# - X Insert at end
	# - X Insert at position
* Deletion:
	- Delete at beginning
	# TODO (below)
	# - X Delete at end
	# - X Delete at position
"""


class SinglyNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next


class SinglyLinkedList:
	def __init__(self, head=None):
		self.head = head

	def __str__(self):
		"""Display"""
		curr = self.head
		vals = []
		while curr:
			vals.append(str(curr.val))
			curr = curr.next
		return " -> ".join(vals)

	def is_empty(self):
		"""Check if empty"""
		return self.head is None

	def length(self):
		"""Get length"""
		curr = self.head
		length = 0
		while curr:
			length += 1
			curr = curr.next
		return length

	def traverse(self):
		"""Traverse list"""
		curr = self.head
		while curr:
			print(curr.val)
			curr = curr.next

	def lookup(self, target):
		"""Lookup a value"""
		curr = self.head
		while curr:
			if curr.val == target:
				return True
			curr = curr.next
		return False

	def modify(self, index, new_val):
		"""Modify a value"""
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

	def del_at_beginning(self):
		"""Delete at beginning"""
		self.head = self.head.next


print('------')
print('Add to beginning of list:')
my_list = SinglyLinkedList()
for i in range(1, 4):
	my_list.insert_at_beginning(SinglyNode(i))
	print(my_list)
print('is empty: ', my_list.is_empty())
print('length: ', my_list.length())


print('\n------')
print('Del at beginning of list:')
for i in range(my_list.length()):
	print(my_list)
	my_list.del_at_beginning()
print('is empty: ', my_list.is_empty())
print('length: ', my_list.length())


print('\n------')
print('Traverse list:')
my_list = SinglyLinkedList()
for i in range(10, 0, -1):
	my_list.insert_at_beginning(SinglyNode(i))
print(f'LIST | {my_list}')
print('traverse:')
my_list.traverse()


print('\n------')
print('Lookup a value:')
print(f'LIST | {my_list}')
print(f'2: {my_list.lookup(2)}')
print(f'8: {my_list.lookup(8)}')
print(f'50: {my_list.lookup(50)}')
print(f'70: {my_list.lookup(70)}')


print('\n------')
print('Modify a value:')
print(f'LIST | {my_list}')
print(f'change index 0 to 100:')
my_list.modify(0, 100)
print(my_list)
print(f'change index 9 to 55:')
my_list.modify(9, 55)
print(my_list)
