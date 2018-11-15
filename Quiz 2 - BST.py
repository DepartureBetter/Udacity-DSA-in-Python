class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_bst(self.root, new_val)

    def search(self, find_val):
        return self.search_bst(self.root, find_val)
                
    def search_bst(self, start, find_val):           
        if start:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                return self.search_bst(start.left, find_val)
            else:
                return self.search_bst(start.right, find_val)
        return False
        
    def insert_bst(self, start, val):
        if start.value < val:
            if start.left:
                self.insert_bst(start.left, val)
            else:
                start.left = Node(val)
        else:
            if start.right:
                self.insert_bst(start.right, val)
            else:
                start.right = Node(val)

            
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)