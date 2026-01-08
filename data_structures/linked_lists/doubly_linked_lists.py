"""
Doubly Linked Lists


----- Operations -----
* Display
* Check if empty
* Get length
* Traverse list
* Lookup a value
* Modify a value
* Get head
* Get tail

* Insertion:
	- Insert at beginning
	- Insert at end
	# - X Insert at position
* Deletion:
	- Delete at beginning
	- Delete at end
	# - X Delete at position
"""


class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return f'{self.val}'
    
    
    
class DoublyLinkedList:
    def __init__(self, head, tail=None):
        self.head = head
        if tail:
            self.tail = tail
            self.head.next = tail
            self.tail.prev = self.head
        else:
            self.tail = head
            
    def display(self):
        '''Display all node values in a clean format'''
        curr = self.head
        vals = []
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        print(' <-> '.join(vals))
            
    def is_empty(self):
        return self.head is None
    
    def get_head(self):
        return self.head.val
    
    def get_tail(self):
        return self.tail.val
    
    def length(self):
        '''Get list length'''
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.next
        return length
    
    def traverse(self):
        '''Traverse and print all values 1 by 1'''
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next
            
    def lookup_value(self, target):
        '''Check if a target value exists in the list'''
        curr = self.head
        while curr:
            if curr.val == target:
                return True
            curr = curr.next
        return False
    
    def modify_value(self, pos, new_val):
        '''Modify the value of a node at the specified position (assuming 0-based)'''
        if pos > (self.length()-1):
            raise IndexError('Invalid index value')
        i = 0
        curr = self.head
        while curr:
            if i == pos:
                curr.val = new_val
            i += 1
            curr = curr.next
            
    def insert_at_beginning(self, node):
        '''Update head'''
        node.next = self.head
        self.head.prev = node
        self.head = node
        
    def insert_at_end(self, node):
        '''Update tail'''
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        
    def del_at_beginning(self):
        '''Remove head'''
        old_head = self.head
        self.head = self.head.next
        self.head.prev = None
        del old_head
        
    def del_at_end(self):
        '''Remove tail'''
        old_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del old_tail
        
    
        
    
A = DoublyNode(3)
dll = DoublyLinkedList(head=A)

print('\n-----------Insertion & Deletion-----------')
print('~~ Current list ~~')
dll.display()
print(f'Head: {dll.get_head()}, Tail: {dll.get_tail()}')

print('\nA. Insert 1, 2 at beginning')
dll.insert_at_beginning(DoublyNode(2))
dll.insert_at_beginning(DoublyNode(1))
dll.display()
print(f'Head: {dll.get_head()}, Tail: {dll.get_tail()}')

print('\nB. Insert 4, 5 at end')
dll.insert_at_end(DoublyNode(4))
dll.insert_at_end(DoublyNode(5))
dll.display()
print(f'Head: {dll.get_head()}, Tail: {dll.get_tail()}')

print('\n3. Delete at beginning')
dll.del_at_beginning()
dll.display()
print(f'Head: {dll.get_head()}, Tail: {dll.get_tail()}')

print('\n4. Delete at end')
dll.del_at_end()
dll.display()
print(f'Head: {dll.get_head()}, Tail: {dll.get_tail()}')



print('\n\n-----------Operations-----------')
print('~~ Current list ~~')
dll.display()

print('\nTraverse list:')
dll.traverse()

print('\nList length: ', dll.length())
print('List is empty: ', dll.is_empty())

print('\nLookup 2 (int): ', dll.lookup_value(2))
print('Lookup 13 (int): ', dll.lookup_value(13))

print('\nModify value at pos 1 to 10 ')
dll.display()
dll.modify_value(pos=1, new_val=10)
dll.display()
