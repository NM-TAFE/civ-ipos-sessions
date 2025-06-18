from src.organisation import Organisation


# project.py
class Project:
    def __init__(self, name, organisation):
        self.name = name
        self.organisation = organisation
        self.contacts = []

    # add contacts
    # Challenge - For a contact to be added to a
    def add_contact(self, contact):
        self.contacts.append(contact)
    # project it must already exist in the organisation

    # TODO add rest of setters
