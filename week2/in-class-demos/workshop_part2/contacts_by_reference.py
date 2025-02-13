# Step debug through the code, each function and the first line of the if statement
# Run the code - note the in built id method uses memory addresses to create a unique id for objects in memory
# Compare the contact list id and the organisation contacts list id
# at the end to further explain pass by object reference

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

def add_contact(contacts, name, email):
    # Create a new Contact object with the provided name and email
    new_contact = Contact(name, email)
    print('new contact id', id(new_contact))
    contacts.append(new_contact)
    print('contact list id', id(contacts))

def modify_contact_name(contact, new_name):
    # Modify the 'name' attribute of the Contact object
    contact.name = new_name
    print('contact id', id(contact))

def display_contacts(contacts):
    for contact in contacts:
        # Display the name, email, and id of each Contact object in the contacts list
        print(f"Name: {contact.name}, Email: {contact.email}")
        print('contact id', id(contact))
        print('contact list id', id(contacts))

if __name__ == "__main__":
    organisation_contacts = []
    print('organisation list id', id(organisation_contacts))  # Print the id of the initial contacts list

    # Add two contacts to the organisation_contacts list
    add_contact(organisation_contacts, "John Doe", "john@example.com")
    add_contact(organisation_contacts, "Alice Smith", "alice@example.com")

    print("Original Contacts:")
    display_contacts(organisation_contacts)

    # Modify the name of the first contact
    modify_contact_name(organisation_contacts[0], "John Updated")

    print("\nContacts after modification:")
    display_contacts(organisation_contacts)
