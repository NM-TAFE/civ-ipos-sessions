'''The following code (run it) demonstrates
what happens when we update mutable and immutable objects
Remember: the id is just the memory address
Remember: the name is *not* the object
'''

print('"Updating" a mutable variables')
input("Ready? Press Enter to start...")
print()
a = 2
print("a = 2")
print('id', id(a))
input()
a = 4
print("a = 4")
print('id', id(a))
input()
a += 1
print("a += 1")
print('id', id(a))
input()
print()
print("Now, let's do a mutable!")
input("Ready? Let's go...")
a = []
print("a = []")
print('id', id(a))
input()
a.append(2)
print("a.append(2)")
print('id', id(a))
input()

a += [1]
print("a += [1]")
print('id', id(a))
input()

print("""
Notice that when we 'update' an immutable
object we are creating a new object
and then updating the named reference
to point to the new object.
When we update a mutable objects, references
do not need to change
""")