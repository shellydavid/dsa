"""
Stacks (LIFO)

----- Operations -----
1. is_empty
2. push
3. pop
4. peek

----- Implementation -----
Because they are Last in First Out,
stacks PUSH to the R and POP from the R

> Dynamic arrays work good, bec
	- adding to the R is amortized *O(1) (resizing is needed, but infrequently)
	- deleting from the R is always O(1)

> Doubly linked list can work too, because modifying the tail is always O(1).
"""


class Stack:
	def __init__(self):
		self.stack = []

	def is_empty(self):
		return len(self.stack) == 0

	def push(self, val):
		self.stack.append(val)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1]


stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)

print(stk.stack)
stk.pop()
print(stk.stack)
stk.pop()
print(stk.stack)
stk.pop()
print(stk.stack)
