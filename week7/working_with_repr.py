class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '🐈' # can be anything that makes sense

    def __repr__(self):
        return f"Cat({self.name!r})" # usually string to create an instance
        # -> !r call repr: Notice how we use reprs all the way down.

c1 = Cat("Lenny")
c2 = Cat("Kenny")
Cat('Kenny')
print(c1, c2)
# Note: a bug in the PyCharm debugger makes it use __str__ over __repr__
# See: https://youtrack.jetbrains.com/issue/PY-35529/Add-Option-to-Use-repr-instead-of-str-in-variables-debugging-view

