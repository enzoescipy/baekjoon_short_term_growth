# Heap Data Structure

A heap is a specialized tree-based data structure that satisfies the **heap property**. Heaps are commonly used to implement priority queues and are fundamental to many algorithms, including Heap Sort, Dijkstra's algorithm, and finding the median of a stream of numbers.

## Types of Heaps

- **Min-Heap**: For every node, the parent's value is less than or equal to its children
- **Max-Heap**: For every node, the parent's value is greater than or equal to its children

## Heap Representation in Arrays

Heaps are typically implemented as arrays (not linked structures) for efficiency. The tree structure is implicitly represented through index arithmetic:

For a node at index `i` (0-based indexing):
- Parent: `(i-1)//2`
- Left Child: `2*i + 1`
- Right Child: `2*i + 2`

Example of a min-heap as both a tree and array:
```
       5              Array: [5, 10, 7, 20, 15, 12, 30]
     /   \                    0   1   2   3   4   5   6
   10     7
  /  \   /  \
 20  15 12   30
```

## Core Heap Operations

### 1. Sift-Up (Bubble-Up)

Used when adding a new element to the heap. The element is first placed at the end of the array and then "bubbled up" to its correct position.

**Visual Example of Sift-Up:**

Let's add the value 2 to this min-heap:
```
       5              Array: [5, 10, 7, 20, 15, 12, 30]
     /   \                    0   1   2   3   4   5   6
   10     7
  /  \   /  \
 20  15 12   30
```

Step 1: Add the new element (2) at the end:
```
       5              Array: [5, 10, 7, 20, 15, 12, 30, 2]
     /   \                    0   1   2   3   4   5   6  7
   10     7
  /  \   /  \
 20  15 12  30
 /
2
```

Step 2: Compare with parent (20) and swap since 2 < 20:
```
       5              Array: [5, 10, 7, 2, 15, 12, 30, 20]
     /   \                    0   1   2  3   4   5   6   7
   10     7
  /  \   /  \
 2   15 12  30
 /
20
```

Step 3: Compare with parent (10) and swap since 2 < 10:
```
       5              Array: [5, 2, 7, 10, 15, 12, 30, 20]
     /   \                    0  1  2   3   4   5   6   7
   2      7
  /  \   /  \
 10  15 12  30
 /
20
```

Step 4: Compare with parent (5) and swap since 2 < 5:
```
       2              Array: [2, 5, 7, 10, 15, 12, 30, 20]
     /   \                    0  1  2   3   4   5   6   7
   5      7
  /  \   /  \
 10  15 12  30
 /
20
```

The sift-up operation is complete as the new element has reached its correct position.

```python
def sift_up(array, index):
    """Move an element up the heap until it satisfies the heap property (iterative approach)"""
    current = index
    parent = (current - 1) // 2
    
    # Continue until we reach the root or heap property is satisfied
    while current > 0 and array[current] < array[parent]:
        # Swap with parent
        array[current], array[parent] = array[parent], array[current]
        # Move up one level
        current = parent
        parent = (current - 1) // 2
```

> [!note]
> This is an iterative implementation of sift-up. Instead of using recursion, we use a while loop to move up the heap until we reach the root or the heap property is satisfied.

### 2. Sift-Down (Bubble-Down)

Used when removing the root element or when building a heap. The last element is moved to the root position and then "bubbled down" to its correct position.

**Visual Example of Sift-Down:**

After removing the root (2) from our min-heap, we replace it with the last element (20):
```
Initial heap:
       2              Array: [2, 5, 7, 10, 15, 12, 30, 20]
     /   \                    0  1  2   3   4   5   6   7
   5      7
  /  \   /  \
 10  15 12  30
 /
20
```

After removing 2 and replacing with 20:
```
      20              Array: [20, 5, 7, 10, 15, 12, 30]
     /   \                    0  1  2   3   4   5   6
   5      7
  /  \   /  \
 10  15 12  30
```

Step 1: Compare with children (5 and 7) and swap with smallest (5):
```
       5              Array: [5, 20, 7, 10, 15, 12, 30]
     /   \                    0  1   2   3   4   5   6
   20     7
  /  \   /  \
 10  15 12  30
```

Step 2: Compare with children (10 and 15) and swap with smallest (10):
```
       5              Array: [5, 10, 7, 20, 15, 12, 30]
     /   \                    0  1   2   3   4   5   6
   10     7
  /  \   /  \
 20  15 12  30
```

The sift-down operation is complete as the element has reached its correct position.

```python
def sift_down(array, index, heap_size):
    """Move an element down the heap until it satisfies the heap property (iterative approach)"""
    current = index
    
    while True:
        smallest = current
        left = 2 * current + 1
        right = 2 * current + 2
        
        # Find smallest among current, left child and right child
        if left < heap_size and array[left] < array[smallest]:
            smallest = left
        
        if right < heap_size and array[right] < array[smallest]:
            smallest = right
        
        # If current is already in the right place, stop
        if smallest == current:
            break
            
        # Otherwise swap and continue downward
        array[current], array[smallest] = array[smallest], array[current]
        current = smallest
```

> [!note]
> This is an iterative implementation of sift-down. We use a while loop that continues until the element is in its correct position (when it's smaller than both its children or it's a leaf node).

### 3. Building a Heap

To build a heap from an arbitrary array, we use a bottom-up approach starting from the last non-leaf node.

```python
def build_heap(array):
    """Transform an arbitrary array into a valid heap in O(n) time"""
    n = len(array)
    # Start from the last non-leaf node
    start_idx = (n // 2) - 1
    
    # Perform sift-down on each node, bottom-up
    for i in range(start_idx, -1, -1):
        sift_down(array, i, n)
```

> [!note]
> Even though build_heap involves O(log n) operations for each of the n/2 nodes, the overall complexity is actually O(n), not O(n log n) due to the mathematical distribution of operations across tree levels.

## Python Implementation with `heapq`

Python's standard library provides the `heapq` module for working with min-heaps:

```python
import heapq

# Create a heap
heap = []

# Add elements (push)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)

print(heap)  # [1, 3, 7, 5] - note this is a valid min-heap!

# Remove the smallest element (pop)
smallest = heapq.heappop(heap)  # returns 1
print(smallest)  # 1
print(heap)  # [3, 5, 7]

# Peek at the smallest without removing
smallest = heap[0]  # returns 3

# Convert an existing list into a heap
nums = [5, 3, 7, 1, 9, 2]
heapq.heapify(nums)  # transforms nums in-place to [1, 3, 2, 5, 9, 7]
```

## Max-Heap in Python

Since Python's `heapq` only provides min-heap functionality, we can simulate a max-heap by negating values:

```python
import heapq

# Create a max heap
max_heap = []

# Add elements (negate values)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -7)
heapq.heappush(max_heap, -1)

# Remove the largest element
largest = -heapq.heappop(max_heap)  # returns 7
```

## Custom Heap Implementation

Here's a complete custom implementation of a min-heap in Python using iterative approaches:

```python
class MinHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
        
    def left_child(self, i):
        return 2 * i + 1
        
    def right_child(self, i):
        return 2 * i + 2
        
    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]
        
    def extract_min(self):
        if not self.heap:
            return None
            
        min_val = self.heap[0]
        
        # Move last element to root
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Fix the heap
        if self.heap:
            self._sift_down(0)
            
        return min_val
        
    def insert(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, i):
        current = i
        parent = self.parent(current)
        
        while current > 0 and self.heap[current] < self.heap[parent]:
            # Swap with parent
            self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            # Move up
            current = parent
            parent = self.parent(current)
            
    def _sift_down(self, i):
        current = i
        heap_size = len(self.heap)
        
        while True:
            smallest = current
            left = self.left_child(current)
            right = self.right_child(current)
            
            if left < heap_size and self.heap[left] < self.heap[smallest]:
                smallest = left
                
            if right < heap_size and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            if smallest == current:
                break
                
            # Swap with smallest child
            self.heap[current], self.heap[smallest] = self.heap[smallest], self.heap[current]
            current = smallest
            
    def build_heap(self, array):
        self.heap = array.copy()
        n = len(self.heap)
        
        # Start from last non-leaf node
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)
```

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Find Min/Max | O(1) |
| Insert | O(log n) |
| Delete Min/Max | O(log n) |
| Build Heap | O(n) |

## Why Use Heaps?

Heaps are optimal when you need to:

1. Repeatedly find the minimum or maximum element
2. Process items in priority order
3. Efficiently maintain a running median
4. Sort items in O(n log n) time with heap sort

## Comparison with Other Data Structures

| Structure | Find Min | Insert | Delete Min | Find | Build |
|-----------|----------|--------|-----------|------|-------|
| Array (unsorted) | O(n) | O(1) | O(n) | O(n) | O(n) |
| Array (sorted) | O(1) | O(n) | O(1) | O(log n) | O(n log n) |
| Heap | O(1) | O(log n) | O(log n) | O(n) | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n log n) |

This makes heaps especially valuable for applications where you need fast access to the minimum/maximum element while still allowing efficient insertions and deletions. 