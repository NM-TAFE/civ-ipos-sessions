# crazy_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
# print(crazy_list[3][1][2][0])
#
# animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']
#
#
# #sequential
# for animal in animals:
#     # check in each object for the string
#     # if it si there
#      if animal == 'Zebra':
#         has_zebra = True
#         break
#     else:
#     # it it isnt there move on
#         has_zebra = False
# try:
#     print(f'LIst contains a zebra? {has_zebra}')
# except ValueError:
#     print('No value found')
#
# print(f"Has zebra?  {"Zebra" in animals}")
#
# animals = tuple(animals)
# animals.append('Bear')

animals = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}
animals['Lion'] = 'King'
print(animals)

animals = set(animals)
print(animals)



# animals

class Animal:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def set_characteristic(self, new_characteristic):
        self.characteristic = new_characteristic
