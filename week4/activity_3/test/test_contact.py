# test_contact.py
import unittest

from src.contact import Contact

class TestContact(unittest.TestCase):

    # Step 2
    # pass
        # Create a contact
    def test_can_create_contact(self):
        contact = Contact('John', 'test@example.com')
        # Check if attributes are set correctly
        self.assertEqual(contact.name, 'John')
        self.assertEqual(contact.email, 'test@example.com')