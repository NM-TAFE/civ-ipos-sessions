# test_organization.py
import unittest
from src.organisation import Organisation
from src.contact import Contact

# Step 1
class TestOrganisation(unittest.TestCase):
    def test_add_organisation(self):
        # Create an organization
        org = Organisation("NM Tafe")
        self.assertEqual(org.name, "NM Tafe")



    # Step 3
    def test_add_contact(self):
        # Create an organisation
        org = Organisation("NM Tafe")
        # Create a contact
        contact = Contact("John R", "john@example.com")
        # Add contact to organisation
        org.add_contact(contact)
        # Check if contact is added to the organisation
        self.assertIn(contact, org.get_contacts())

if __name__ == '__main__':
    unittest.main()