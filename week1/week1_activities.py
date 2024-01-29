crazy_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print('Actual:', crazy_list[3][1][2][0], "Guess: hello")

animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']

# key concepts:
# sequential versus random access
# (new terms, not new concepts)

# does the list contain Zebra: sequential!
for animal in animals:
    if animal == 'Zebra':
        "Found it!"
        break
else:
    "No Zebras here!"

# how we do it:
try:
    animals.index('Zebra')
except ValueError:
    print("No Zebras found")

# best:
print("Has Zebra", "Zebra" in animals)

print("Is Giraffe in 2?", "Giraffe" == animals[2])

animals.append('Zebra')
animals.remove('Cheetah')

# typo!


animals = tuple(animals)
# animals.append('Bear')  # Uncommenting this will throw an error because tuples are immutable!
#                           (actually, it's because tuples don't have an append method because they are immutable)

animals_dict = {'Lion': 'Brave',
               'Tiger': 'Fierce',
               'Elephant': 'Large',
               'Giraffe': 'Tall',
               'Zebra': 'Striped'}

animal_names = []
for name in animals_dict:
    animal_names.append(name)

# better (but identical):
animal_names = [name for name in animals_dict]

animal_c = []
for value in animals_dict.values():
    animal_c.append(value)

# better
animal_c = [value for value in animals_dict.values()]

animals = {}
for n, c in zip(animal_names, animal_c):
    animals[n] = c

# better (but same)
animals = {names: c
            for names, c in zip(animal_names, animal_c)}

animals['Lion'] = 'King'


class Animal:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def modify_characteristic(self, new_characteristic):
        self.characteristic = new_characteristic

lion = Animal('Lion', 'King')
lion.modify_characteristic('Brave')

animal_classes = {}
for k, v in animals.items():
    animal_classes[k] = Animal(k, v)

# or as a comprehension:

animal_classes = [Animal(a, c)
                  for a, c in animals.items()]


