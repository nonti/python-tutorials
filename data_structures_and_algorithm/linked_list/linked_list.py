# 1. Node Class:
class Node:
    def __init__(self, data):
        self.data = data  # Store data in the node
        self.next = None  # Pointer to the next node (initially None)

# 2. CircularList Class:
class CircularList:
    def __init__(self):
        self.head = None  # Initialize an empty circular list with no head
    
    # Insert a new node into the circular linked list
    def insert(self, data):
        new_node = Node(data)  # Create a new node with the provided data
        
        # If the list is empty, set the new node as the head and make it circular
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point next to itself to make it circular
        else:
            # Traverse to the last node in the list
            current = self.head
            while current.next != self.head:
                current = current.next
            
            # Insert the new node at the end and link it back to the head
            current.next = new_node
            new_node.next = self.head
    
    # Display the elements of the circular linked list
    def display(self):
        if self.head is None:
            print("Circular List is empty.")
            return
        
        current = self.head
        print("Circular List:", end=" ")
        
        # Traverse through the list until we reach the head again
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:  # If we are back at the head, stop
                break
        print()

# 3. Call the CircularList:
circular_list = CircularList()

# Insert nodes with data 1, 2, and 3 into the circular linked list
circular_list.insert(1)
circular_list.insert(2)
circular_list.insert(3)

# Display the elements of the circular linked list
circular_list.display()
