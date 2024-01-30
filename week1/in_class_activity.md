# **Workshop**: Python’s Data Structures and Classes

## Warm-up

Here's a bit of a warm-up:

What will be the output of this code snippet?

```python
crazy_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(crazy_list[3][1][2][0])
```

Think of an answer before you run the code. When you think you know - run the code!

## Lists and Tuples

Create a list representing a pack of animals:

```python
animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']
```

Here is an example of **sequential access**:

```python
for animal in animals:
    print(animal)
```

Here is an example of **random access** (let's get the third animal in the pack):

```python
print(animals[2])  # Remember Python uses zero-based indexing!
```

### Challenges

1. Use sequential access to check if the list contains a Zebra
2. What is the correct way to check if a list contains a Zebra? How do you stop it from raising an exception (two correct answers)
3. Use random access to see if the second element is a Giraffe

Good!

Now, let's add a 'Zebra' to the pack and remove 'Cheetah':

```python
animals.append('Zebra')
animals.remove('Cheetah')
```

Finally, let's convert this list to a tuple and try to add 'Bear' to the pack:

```python
animals = tuple(animals)
# animals.append('Bear')  # Uncommenting this will throw an error because tuples are immutable!
```

## Dictionaries and Sets

We'll convert the animal pack list to a dictionary where the animal is the key and its characteristic is the value:

```python
animals = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}
```

### Challenges 2

Build a list of characteristics and a list of animals, and then use the two lists to create a dictionary of animals and their characteristic.
Try using `zip`; try using a list comprehension.

Let's modify the characteristic of 'Lion' to 'King':

    animals['Lion'] = 'King'

We'll also convert our pack list to a set, which only contains unique elements:

    animals = set(pack_list)

Try adding 'Lion' again to the set and see what happens:

    animals.add('Lion')  # Nothing changes because 'Lion' is already in the set!

## Classes in Python

We'll now create an 'Animal' class. Each object will represent an animal from the pack:

    class Animal:
        def __init__(self, name, characteristic):
            self.name = name
            self.characteristic = characteristic

        def modify_characteristic(self, new_characteristic):
            self.characteristic = new_characteristic

    lion = Animal('Lion', 'King')
    lion.modify_characteristic('Brave')

### Challenges 3

Now, sequentially access the `items` in the animals dictionary to create an instance of each of the animals with its corresponding characteristics.

## Data Structures vs. Classes: A Comparative Analysis

Let's discuss the pros and cons of each representation:

- **Lists, Tuples, and Sets**: These are great for storing a collection of items, especially when the order of items matters (lists and tuples) or when you want to eliminate duplicates (sets). However, they don't offer a straightforward way to associate additional information with each item (like our 'characteristics' for animals).
- **Dictionaries**: These are excellent for associating pairs of information (like our animals and their characteristics). However, they lack order (prior to Python 3.7) and don't provide a way to associate methods with the data.
- **Classes**: These are the most flexible as they can encapsulate data (like animal names and characteristics) and methods (like modifying characteristics). However, they require more upfront design and planning.
