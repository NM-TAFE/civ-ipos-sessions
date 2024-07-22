# Python Pass-By-Object Reference Cheatsheet

## Basic Concepts

- **Immutable Types**: `int`, `float`, `str`, `tuple`
- **Mutable Types**: `list`, `dict`, `set`

## Immutable Objects

1. **Reassignment**: Reassigning an immutable object creates a new memory location.

   ```python
   x = 42
   y = x
   x = 43  # y is still 42
   ```

2. **Function Argument**: Immutable objects don't change when passed into a function.

   ```python
   def update_value(num):
       num = 99
   
   x = 42
   update_value(x)  # x is still 42
   ```

## Mutable Objects

1. **In-Place Modification**: Changing a mutable object affects all references to that object.

   ```python
   x = [1, 2, 3]
   y = x
   x.append(4)  # y is now [1, 2, 3, 4]
   ```

2. **Function Argument**: Mutable objects can be modified inside a function, affecting the original object.

   ```python
   def update_list(lst):
       lst.append(4)
   
   x = [1, 2, 3]
   update_list(x)  # x is now [1, 2, 3, 4]
   ```

## Function Return

- **Immutable**: If a function returns an immutable object, you must explicitly capture the returned value.

  ```python
  def add_value(num):
      return num + 1
  
  x = 42
  x = add_value(x)  # x is now 43
  ```

- **Mutable**: If a function modifies a mutable object, no need to capture the return unless creating a new object.

  ```python
  def new_list(lst):
      return lst + [4]
  
  x = [1, 2, 3]
  x = new_list(x)  # x is now [1, 2, 3, 4]
  ```

## Common Pitfalls

1. **Default Mutable Arguments**: Avoid using mutable defaults in function arguments.

   ```python
   # Don't
   def add_item(item, lst=[]):
       lst.append(item)
       return lst
   
   # Do
   def add_item(item, lst=None):
       if lst is None:
           lst = []
       lst.append(item)
       return lst
   ```

2. **Shallow Copy**: Be aware that shallow copies (`copy.copy()`, `list[:]`) create new objects but don't deep-copy nested objects.

   ```python
   import copy
   x = [[1], [2]]
   y = copy.copy(x)
   y[0].append(10)  # x is now [[1, 10], [2]]
   ```

## Summary

- Immutable objects are effectively passed by value.
- Mutable objects are effectively passed by reference.
- But both types are in practice "pass-by-object-reference" - that is the parameter passing mechanism is identical.
- Because functions can modify mutable arguments but must create new instances for immutable arguments (which are only referenced by local names unless a global keyword is used).
  
