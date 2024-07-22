crazy_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(crazy_list[3][1][2][0])

animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']
# key concepts:
# sequential versus random access
# (new terms, not new concepts)

# does the list contain Zebra: sequential!

for animal in animals:
    if animal == 'Zebra':
        has_zebra = True
        break
    else:
        has_zebra = False

# print(f"List contains Zebra?", has_zebra)

# # how we do it:
try:
    animals.index('Zebra')
except ValueError:
    print("No Zebras found")

# # best:
# print("Has Zebra",  "Zebra" in animals)

# print("Is giraffe in 2?", "Giraffe" == animals[2])

# # typo!

# animals = tuple(animals)
# # animals.append('Bear')  # Uncommenting this will throw an error because tuples are immutable!
# #                           (actually, it's because tuples don't have an append method because they are immutable)

animals_dict = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}

animal_names = []
for name in animals_dict:
    animal_names.append(name)

# # better (but identical):
animal_names = [name for name in animals_dict.keys()]

# animal_characteristics = []
# animal_names = list(animals_dict.keys())
# animal_characteristics = list(animals_dict.values())

# animal_characteristics = []
# for value in animals_dict.values():
#     animal_characteristics.append(value)

# # # better (but identical)
animal_characteristics = []
animal_characteristics = [value for value in animals_dict.values()]

animals = {}

# watch this zip object
for n, c in zip(animal_names, animal_characteristics):
    animals[n] = c
# # better (but same)
# # or as a comprehension:
# animals = {n:c for n, c in zip(animal_names, animal_characteristics)}

animals['Lion'] = 'King'


# # take a look at the key in the set
# animals_set = set(animals)

# print(animals_set)

class Animal:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def modify_characteristics(self, new_characteristic):
        self.characteristic = new_characteristic


lion = Animal('Lion', 'King')

## For review and test during for week 2
lion.modify_characteristics('Brave')

animal_classes = {}
for key, value in animals.items():
    animal_classes[key] = Animal(key, value)

animal_classes = [Animal(a, c)
                  for a, c in animals.items()]

print(animal_classes)