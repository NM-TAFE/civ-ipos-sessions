# organisation.py
# TODO: Step1
class Organisation:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    # TODO Step 3 get & set contacts (add and retrieve)
    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts
