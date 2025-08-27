# test_organization.py
import unittest

from src.contact import Contact
from src.organisation import Organisation

# Create an organization
class TestOrganisation(unittest.TestCase):
    # test that we create a name
    # arrange
    def test_add_organisation(self):
        # act
        org = Organisation('Johns Org')
        # assert
        self .assertEqual(org.name, 'Johns Org')

    # pass

    # Step 3 - test can add a contact
    def test_can_add_a_contact(self):
        # Create an organisation
        org = Organisation('Johns Org')
        # Create a contact
        contact = Contact('John', 'test@example.com')
        # Add contact to organisation
        org.add_contact(contact)
        # Check if contact is added to the organisation
        self.assertIn(contact, org.contacts)
