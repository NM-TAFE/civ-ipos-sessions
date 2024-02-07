# Lesson Overview
Introduction to intermediate concepts:
- Modular programming
- Pass-by-reference
- (optional) Intro to 2D data structures

## Objectives
1. Understand the mechanics and reasoning for 
modular programming in Python
2. Understand pass-by-reference and its application in Python
3. Apply your knowledge to practical and synthetic problems


# Outcome

- Be able to answer the following questions:

1. What is a module in Python? How do you create one?
2. What is the purpose of the import statement in Python? Can you provide a code example of its usage?
3. How can you import only a specific function or class from a module in Python? What is the syntax for this?
4. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference?
5. Given the following Python code, what will be the output and why?
```python
def modify_list(lst):
    lst.append("new")
    lst = ["completely", "new"]

items = ["original"]
modify_list(items)
print(items)
```

6. If Python uses pass-by-reference, why doesn't reassigning a variable inside a function change the original variable outside the function? How is this related to the mutability of Python objects?

- Be able to refactor non-modular code into modular alternatives.
