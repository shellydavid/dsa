
''' Linked List '''
# Reverse a linked list
# Time: O(n)
# Space: O(n) - the call stack will store everything until it reaches the end/base case (NULL)

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def __str__(self):
        return f"{self.value}"

head = Node(0)
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

head.next = A
A.next = B
B.next = C
C.next = D

# Traverse the list:
node = head
while node is not None:
    print(node)
    node = node.next

# Reverse the list (recursively):
def reverse(node):
    if node is None:
        return 
    reverse(node.next)
    print(node)

print('\n----------------------')
reverse(head)
    


''' Factorial '''
# Time: O(n)
# Space: O(n)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)  # Each function call makes one other recursive call, no branching - so its O(n)

print('\n----------------------')
print('3! = ', factorial(3))
print('4! = ', factorial(4))
print('5! = ', factorial(5))
