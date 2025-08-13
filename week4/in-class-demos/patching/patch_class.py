from unittest import TestCase
from unittest.mock import patch
from contact_module import create_contact


class TestCreateContact(TestCase):
    @patch('contact_module.Contact')  # Mock the Contact class in the contact_module
    def test_create_contact(self, MockContact):
        """
        Ensure create_contact correctly instantiates a Contact object
        with the provided name and email, and returns it.
        """
        # Arrange: Set up expected input
        name = 'John'
        email = 'john@example.com'

        # Act: Call the function under test
        contact = create_contact(name, email)

        # Assert: Verify Contact was instantiated with correct arguments
        MockContact.assert_called_once_with(name, email)

        # Assert: The returned object is the mocked instance
        self.assertEqual(contact, MockContact.return_value)


if __name__ == "__main__":
    import unittest
    unittest.main()
