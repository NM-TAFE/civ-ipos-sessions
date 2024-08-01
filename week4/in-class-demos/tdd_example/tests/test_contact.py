# test_contact.py
import unittest

from src.contact import Contact

class TestContact(unittest.TestCase):
    # Step 1
    def test_contact_creation(self):
        # Create a contact
        contact = Contact("John Doe", "john@example.com")
        # # Check if attributes are set correctly
        self.assertEqual(contact.name, "John Doe")
        self.assertEqual(contact.email, "john@example.com")

if __name__ == '__main__':
    unittest.main()

