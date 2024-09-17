import heapq

class MaxHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []

    def insert(self, element):
        # Insert the negation of the element to simulate a max-heap
        heapq.heappush(self.heap, -element)

    def extract_max(self):
        # Extract the negation of the maximum element, then negate it back
        if not self.heap:
            raise IndexError("extract_max(): heap is empty")
        return -heapq.heappop(self.heap)

# Example usage:
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(15)

print(max_heap.extract_max())  # Output: 20
print(max_heap.extract_max())  # Output: 10

