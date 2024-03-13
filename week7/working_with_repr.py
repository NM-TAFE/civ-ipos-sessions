# The __str__ method returns a string representation of an object that is human-readable while the __repr__ method returns a string representation of an object that is machine-readable.

# In debugging, you can use __repr__ to provide more meaningful information about the state of an object 
# when you print it or inspect it during debugging sessions. For instance, if you have a complex object and you want to see its internal state while debugging, you can define a __repr__ method that provides a concise and informative string representation of that object

class Cat:
    def __init__(self, name):
        self.name = name
    # The __str__ method returns a fixed string '🐈', which will be used when you directly print the object or use str() function on it.
    def __str__(self):
        return '🐈' # can be anything that makes sense

    # The __repr__ method returns a string representation of the object, including its name. 
    # This method is used when you want to create an instance of the object using its representation.
    def __repr__(self):
        return f"Cat({self.name!r})" # usually string to create an instance
        # -> !r call repr: Notice how we use reprs all the way down.
    

# When you create instances of the Cat class (c1 = Cat("Lenny") and c2 = Cat("Kenny")), 
# the __repr__ method is implicitly called to create the string representation of the objects.
c1 = Cat("Lenny")
c2 = Cat("Kenny")

# The line Cat('Kenny') creates a new Cat object but doesn't assign it to any variable. 
# This line will call the __repr__ method to create the string representation.
Cat('Kenny')

# Finally, when you print c1 and c2, the __str__ method is called for string conversion 
# because it's the default behavior for printing. 
# However, if you directly access c1 or c2 in a debugging environment, the __repr__ method will be used to display their representations.

print(c1, c2)


# Note: a bug in the PyCharm debugger makes it use __str__ over __repr__
# See: https://youtrack.jetbrains.com/issue/PY-35529/Add-Option-to-Use-repr-instead-of-str-in-variables-debugging-view

