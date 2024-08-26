# Revision: docstrings versus multiline strings
# I am a comment
"I might be a docstring"
"""I am more likely to be a docstring, but still just a multiline string"""

class Cat:
    """Docstring for cat... best animal in the world"""

    def meow(self, length):
        """Docstring for a method or function"""

    """Remember: a multiline string anywhere else is just a string
    I am just a string, for example."""


print(help(Cat.meow)) # free help, free hover actions, free to gen doc
