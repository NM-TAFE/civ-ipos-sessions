# Data Structures

| Data Structure   | Brief Description             | Built-in? | Usage                  | Representation         | Syntax        |
|------------------|-------------------------------|-----------|------------------------|------------------------|---------------|
| List             | Ordered, dynamic array        | Yes       | General-purpose        | Array                  | `[1, 2, 3]`   |
| Linked List      | Nodes with data and pointers  | No        | Sequential access      | Object references      | N/A           |
| Array            | Fixed-size, same-type elements| No        | Numerical computation  | Contiguous memory      | N/A           |
| Hash Table       | Key-Value storage             | Yes       | Associative mapping    | Array of linked lists  | `{'a': 1}`    |
| Set              | Unique, unordered elements    | Yes       | Set operations         | Hash Table             | `{1, 2, 3}`   |
| Tree             | Hierarchical structure        | No        | Tree traversal, sort   | Node references        | N/A           |
| Graph            | Nodes connected by edges      | No        | Network representation | Adjacency List/Matrix  | N/A           |
| Stack            | LIFO structure                | No        | Backtracking, parsing  | Array/Linked List      | N/A           |
| Queue            | FIFO structure                | No        | Scheduling, BFS        | Array/Linked List      | N/A           |
| User-Defined     | Custom data structure         | No        | Specialized tasks      | Varies                 | N/A           |

## Examples

### List

```python
my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]
```

### Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Array

```python
from array import array
arr = array('i', [1, 2, 3])
```

### Hash Table

```python
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # {'a': 1, 'b': 2, 'c': 3}
```

### Set

```python
my_set = {1, 2, 3}
my_set.add(4)  # {1, 2, 3, 4}
```

### Tree

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### Graph

```python
# Using adjacency list
graph = {'A': ['B', 'C'], 'B': ['A', 'D']}
```

### Stack

```python
stack = []
stack.append(1)  # [1]
stack.pop()  # []
```

### Queue

```python
from collections import deque
queue = deque([1, 2])
queue.append(3)  # deque([1, 2, 3])
queue.popleft()  # deque([2, 3])
```

### User-Defined

```python
class CustomStack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size
```
