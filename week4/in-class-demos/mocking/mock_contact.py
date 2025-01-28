
import unittest
from unittest.mock import Mock


class Contact:
    def __init__(self, name, address, billing_details):
        self.name = name
        self.address = address
        self.billing_details = billing_details


def get_contact_info(name):
    # ... code to fetch contact info from a database or API
    pass


# Test class
class TestWeather(unittest.TestCase):
    def test_get_contact_info(self):
        # Mock the real API call
        get_contact_info = Mock(return_value=Contact(
            name="John Doe",
            address={"city": "New York", "state": "NY", "zip": "10001"},
            billing_details={"card_type": "Visa", "expiration_date": "12/25"}
        ))

        self.result = get_contact_info("John Doe")
        print(self.result.name)
        assert self.result.name == "John Doe"
        assert self.result.address == {"city": "New York", "state": "NY", "zip": "10001"}
        assert self.result.billing_details == {"card_type": "Visa", "expiration_date": "12/25"}
