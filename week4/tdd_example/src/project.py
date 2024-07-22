# project.py

class Project:
    def __init__(self, name, organisation):
        self.name = name
        self.organisation = organisation
        # Challenge solution
        self.contacts = []

    # Challenge - define a function from your tests that:
    # adds a contact to project
    # throws an error if the contact is not part of the organisation
    # append the new contact to the contacts list

    # Challenge - Solution# For a contact to be added to a
    # project it must already exist in the organisation
    def add_contact(self, contact):
        if contact not in self.organisation.contacts:
            raise ValueError("Contact must belong to the organisation.")
        self.contacts.append(contact)

