# organisation.py
# TODO attributes for org: name
# TODO behaviours for org: addContact()
class Organisation:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts
 
# many contacts