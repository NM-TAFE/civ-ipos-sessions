# organisation.py
class Organisation:
    # TODO: Step1
    # TODO attributes for org: name
    def __init__(self, name):
        self.name = name
        self.contacts = []
    # pass

    # TODO Step 3 get & set contacts (add and retrieve)
    # TODO behaviours for org: addContact()
    def add_contact(self, contact):
        self.contacts.append(contact)

 
# many contacts
