# test_organization.py
import unittest
from src.organisation import Organisation
from src.contact import Contact

# Step 1
class TestOrganisation(unittest.TestCase):
    # test that we create a name
    def test_create_organisation(self):
        org = Organisation('NM Tafe')
        self.assertEqual(org.name, 'NM Tafe')

    def test_add_contact(self):
        # arrange
        org = Organisation('NM Tafe')
        contact = Contact('John', 'test@example.com')

        # act
        org.add_contact(contact)
        #assert
        self.assertIn(contact, org.get_contacts())

    # def test_get_contacts(self):
        

if __name__ == '__main__':
    unittest.main()