class Node:
    def __init__(self, data):
        """Initialize the node with 'data' and set 'left' and 'right' to None"""
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        """Retrieve the data of the node"""
        return self.data

    def set_data(self, data):
        """Update the data of the node"""
        self.data = data

class BinarySearchTree:
    def __init__(self):
        """Initialize the binary search tree with an empty 'root'"""
        self.root = None

    def insert(self, data):
        """Insert a new node with the given 'data' into the appropriate position"""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        """Helper method to recursively insert a new node in the appropriate position"""
        if data < node.get_data():
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        elif data > node.get_data():
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def search(self, data):
        """Search for the 'data' in the binary search tree"""
        return self._search(self.root, data)

    def _search(self, node, data):
        """Helper method to recursively search for a specific data in the tree"""
        if node is None:
            return False
        if node.get_data() == data:
            return True
        elif data < node.get_data():
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def in_order_traversal(self):
        """Perform in-order traversal and return the elements as a list"""
        elements = []
        self._in_order_traversal(self.root, elements)
        return elements

    def _in_order_traversal(self, node, elements):
        """Helper method to recursively perform in-order traversal and append elements to a list"""
        if node is not None:
            self._in_order_traversal(node.left, elements)
            elements.append(node.get_data())
            self._in_order_traversal(node.right, elements)
# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert elements into the binary search tree
elements_to_insert = [5, 3, 7, 2, 4, 6, 8]
for element in elements_to_insert:
    bst.insert(element)

# Display the elements of the tree in in-order traversal
print(bst.in_order_traversal())  # Output should be [2, 3, 4, 5, 6, 7, 8]

# Search for specific elements
print(bst.search(4))  # Output should be True
print(bst.search(9))  # Output should be False
