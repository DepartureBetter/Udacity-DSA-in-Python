# Actual QUIZ

"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


# 1. Node object
# 2. LinkedList object
# 3. append an element to the end of linked list
# 4. get_postion function which return an element if present at that particular position.
# 5. insert an element at a given position
# 6. Delete an element whose value is given.

class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def append(self, new_element):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	def get_position(self, position):
		pos = 1; current = self.head
		if position > 0 and self.head:
			while current.next and pos < position:
				current = current.next
				pos += 1
			if pos == position:
				return current
			else:
				return None
		else:
			return None


	def insert(self, new_element, position):
		pos = 1; current = self.head
		if self.head:
			if position > 1:
				while current.next and pos < position-1:
					current = current.next
					pos += 1
				new_element.next = current.next
				current.next = new_element
			elif positon == 1:
				new_element.next = self.head
				self.head = new_element
		else:
			self.head = new_element

	def delete(self, value):
		current = self.head; previous = None
		if self.head:
			while current.next and current.value != value:
				previous = current
				current = current.next
			if current.value == value:
				if previous and current.next:
					previous.next = current.next
					current.next = None
				elif previous:
					previous.next = None
				else:
					self.head = current.next
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value


def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data); current = head; pos = 0
    if head:
        if position > 1:
            while current.next and pos < position - 1:
                current = current.next
                pos += 1
            node.next = current.next
            current.next = node
            return head            
        elif position == 1:
            node.next = head.next
            head = node
            return head
    else:
        head = data
        return head

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head


	def append(self, new_element):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	# I can also implement replace a node at a given function hmm. Very very similar to insert
	def insert(self, new_element, position):
		current, pos = self.head, 0
		if self.head:
			if position == 0:
				new_element.next = self.head
				self.head = new_element
			else:
				while current.next and pos < position - 1:
					current = current.next
					pos += 1
				new_element.next = current.next
				current.next = new_element
		else:
			self.head = new_element

	# Brilliant way to reduce the number of lines of code Rohan! Python does return None by default for a function!
	# And what a nice trick to use current in while instead of current.next for condition checking!
	def get_position(self, position):
		current, pos = self.head, 0
		if self.head:
			while current and pos < position:
				current = current.next 
				pos += 1
			return current


	# This code is so much better than my previous code lol! These last 45 minutes have been really good
	# as I improved on a lot of my previoius code. Loving it!
	def delete(self, value):
		current, previous = self.head, None
		if self.head:
			if current.value == value:
				self.head = current.next
				current.next = None
			else:
				while current.next and current.value != value:
					current = current.next
				if current.value == value:
					previous.next = current.next
					current.next = None




		