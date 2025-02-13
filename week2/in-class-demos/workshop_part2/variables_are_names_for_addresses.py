# '''The following code (run it) demonstrates
# what happens when we update mutable and immutable objects
# Remember: the id is just the memory address
# Remember: the name is *not* the object
# Note: add id(a) to your watch list
# '''
#
# print('"Updating" a mutable variables')
# input("Ready? Press Enter to start...")
# print()
# a = 2
# print("a = 2")
# print('id', id(a))
# input()
# a = 4
# print("a = 4")
# print('id', id(a))
# input()
# a += 1
# print("a += 1")
# print('id', id(a))
# input()
# print()
# print("Now, let's do a mutable!")
# input("Ready? Let's go...")
# a = []
# print("a = []")
# print('id', id(a))
# input()
# a.append(2)
# print("a.append(2)")
# print('id', id(a))
# input()
#
# a += [1]
# print("a += [1]")
# print('id', id(a))
# input()
#
# print("""
# Notice that when we 'update' an immutable
# object we are creating a new object
# and then updating the named reference
# to point to the new object.
# When we update a mutable objects, references
# do not need to change
# """)

myList = [3, [55, 44], (4, 8, [100, 120])]
print(id(myList[2]))
newList = myList[:]
print(id(newList))
print(id(myList))
print(myList == newList)
print(myList is newList)
print(myList[2][2].append(180))
# myList[2] = [100, 150, 200]
print(myList[2])

