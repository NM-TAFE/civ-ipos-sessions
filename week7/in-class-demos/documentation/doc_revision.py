# Revision: docstrings versus multiline strings
# TODO show doc variable
# I am a comment
# "I might be a docstring"
"""I am more likely to be a docstring, but still just a multiline string"""

class Cat:
    """Docstring for cat... best animal in the world"""

    def meow(self, length):
        """Docstring for a method or function"""
        pass

    def print_docs(self):
        print(f"{__doc__}")

    """Remember: a multiline string anywhere else is just a string
    I am just a string, for example."""


print(help(Cat.meow))

cat = Cat()
print(cat.print_docs())
