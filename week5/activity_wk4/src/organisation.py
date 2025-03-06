# organisation.py
class Organisation:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    # TODO add rest of setters
    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts
