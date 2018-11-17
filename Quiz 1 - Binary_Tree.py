class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root=None):
        self.root = Node(root)
    
    def search(self, value):
        return self.preorder_search(self.root, value)
    
    def print_tree(self):
        return self.preorder_traversal(self.root, '')[:-1]
        
    def preorder_search(self, curNode, value):
        if curNode:
            if curNode.value == value:
                return True
            else:
                return self.preorder_search(curNode.left, value) or self.preorder_search(curNode.right, value)
        return False
    
    def preorder_traversal(self, curNode, traversal):
        if curNode:
            traversal += str(curNode.value) + '-'
            traversal = self.preorder_traversal(curNode.left, traversal)
            traversal = self.preorder_traversal(curNode.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()



class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Know how to insert a tree in a balanced manner baby!!!!!!	
def insert(self, value):
	if self.root:
		q = [self.root]
		while q:
			node = q.pop(0)
			if node.left:
				q.append(node.left)
			else:
				node.left = Node(value)
				break
			if node.right:
				q.append(node.right)
			else:
				node.right = Node(value)
				break
	else:
		self.root = Node(value)		

class BinaryTree(object):
    def __init__(self, root=None):
        self.root = Node(root)
    
    def search(self, value):
        return self.preorder_search(self.root, value)
        
    def print_tree(self):
        return self.preorder_traversal(self.root, '')[:-1]
    def preorder_search(self, node, value):
        if node:
            if node.value == value:
                return True
            else:
                return self.preorder_search(node.left, value) or self.preorder_search(node.right, value)
        return False
        
    def preorder_traversal(self, node, traversal):
        if node:
            traversal += str(node.value) + '-'
            traversal = self.preorder_traversal(node.left, traversal)
            traversal = self.preorder_traversal(node.right, traversal)
        return traversal
		
class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = left
		self.right = right
		
class BinaryTree(object):
	def __init__(self, root=None):
		self.root = Node(root)
	
	def search(self, val):
		return self.preorder_search(self.root, val)
	
	def insert(self, value):
		if self.root:
			cur = self.root
			q = [cur]
			while q:
				node = q.pop(0)
				if node.left:
					q.append(node.left)
				else:
					node.left = Node(value)
					node = None
				if node.right:
					q.append(node.right)
				else:
					node.right = Node(value)
					node = None
		else:
			self.root = Node(value)
	
	def preorder_search(self, node, value):
		if node:
			if node.value == value:
				return True
			else:
				return self.preorder_search(node.left, value) or self.preorder_search(node.right, value)
		return False
	
	def print_tree(self):
		return self.preorder_traversal(self.root, '')[:-1]
		
	def preorder_traversal(self, start, traversal):
		if start:
			traversal += str(start.value) + '-'
			traversal = self.preorder_traversal(start.left, traversal)
			traversal = self.preorder_traversal(start.right, traversal)
		return traversal
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	