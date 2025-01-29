from unittest import TestCase
from unittest.mock import patch

# Assuming contact_module.Contact and contact_module.create_contact exist
from contact_module import create_contact


class TestCreateContact(TestCase):
    @patch('contact_module.Contact')  # Mocking the Contact class in the contact_module
    def test_create_contact(self, MockContact):
        """
        Test the create_contact function to ensure it creates a Contact
        instance correctly and returns the object with the expected attributes.
        """
        # Create a mock instance of Contact
        mock_contact_instance = MockContact.return_value
        mock_contact_instance.name = 'Alice'
        mock_contact_instance.email = 'alice@example.com'

        # Call the function under test
        # The actual implementation of create_contact should create a Contact instance
        contact = create_contact('Alice', 'alice@example.com')

        # Assert that the Contact class was called with the correct parameters
        MockContact.assert_called_once_with('Alice', 'alice@example.com')
        print(contact)

        # Assert that the returned object has the expected attributes
        self.assertEqual(contact.name, 'Alice')
        self.assertEqual(contact.email, 'alice@example.com')


if __name__ == "__main__":
    import unittest

    unittest.main()
