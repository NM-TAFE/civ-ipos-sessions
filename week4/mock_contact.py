from unittest.mock import Mock

class Contact:
    def __init__(self, name, address, billing_details):
        self.name = name
        self.address = address
        self.billing_details = billing_details

def get_contact_info(name):
    # ... code to fetch contact info from a database or API
    pass

def test_get_contact_info():
    # Mock the real API call
    get_contact_info = Mock(return_value=Contact(
        name="John Doe",
        address={"city": "New York", "state": "NY", "zip": "10001"},
        billing_details={"card_type": "Visa", "expiration_date": "12/25"}
    ))

    result = get_contact_info("John Doe")
    print(result.name)
    assert result.name,"John Doe"
    assert result.address == {"city": "New York", "state": "NY", "zip": "10001"}
    assert result.billing_details == {"card_type": "Visa", "expiration_date": "12/25"}
