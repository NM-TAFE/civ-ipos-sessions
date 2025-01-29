# contact_module.py

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email


def create_contact(name, email):
    """
    Creates a new Contact instance with the given name and email.

    :param name: The name of the contact
    :param email: The email of the contact
    :return: A new Contact instance
    """
    return Contact(name, email)
