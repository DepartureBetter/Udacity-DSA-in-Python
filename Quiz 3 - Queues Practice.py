class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def append(self, new_element):
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	def delete_first(self):
		if self.head:
			deleted = self.head
			self.head = self.head.next
			return deleted.value

	'''def delete_last(self):
		if self.head:
			current, previous = self.head, self.head
			while current.next:
				previous = current
				current = current.next
			previous.next = None
			return current'''

	'''def insert_first(self, new_element):
		if self.head:
			new_element.next = self.head
			self.head = new_element
		else:
			self.head = new_element'''

	def head_is(self):
		if self.head:
			return self.head.value

class Queue(object):
	def __init__(self, head=None):
		self.ll = LinkedList(head)

	def enqueue(self, new_element):
		self.ll.append(new_element)

	def dequeue(self):
		return self.ll.delete_first()

	def peek(self):
		return self.ll.head_is()


# Setup
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

q = Queue(n1)
q.enqueue(n2)
q.enqueue(n3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(n4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(n5)
# Should be 5
print q.peek()



"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0] 

    def dequeue(self):
        return self.storage.pop(0)
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()