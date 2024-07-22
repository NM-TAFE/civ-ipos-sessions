# test_organization.py

import unittest
from src.organisation import Organisation
from src.contact import Contact

class TestOrganization(unittest.TestCase):
    def test_add_organisation(self):
        # Create an organization
        org = Organisation("NM Tafe")



    def test_add_contact(self):
        # Create an organization

        org = Organisation("NM Tafe")
        # Create a contact
        contact = Contact("John Doe", "john@example.com")
        # Add contact to organization
        org.add_contact(contact)
        # Check if contact is added to the organization
        self.assertIn(contact, org.get_contacts())

if __name__ == '__main__':
    unittest.main()
