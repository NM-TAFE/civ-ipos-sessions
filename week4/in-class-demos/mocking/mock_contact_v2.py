import json
import os
import unittest
from dataclasses import dataclass
from typing import Optional


@dataclass
class Contact:
    name: str
    address: dict
    billing_details: dict


def get_contact_info(name: str, db_path: str = "contacts.json") -> Optional[Contact]:
    """
    Loads contacts from a JSON file and returns a Contact by name.
    JSON shape example:
    {
      "John Robbo": {
        "address": { "city": "...", "state": "...", "postcode": "..." },
        "billing_details": { "card_type": "...", "expiration_date": "..." }
      }
    }
    """
    # Check file has been created during setup
    if not os.path.exists(db_path):
        return None

    try:
        with open(db_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        # JSON structure isn't right; treat as "not available"
        return None

    # Retrieve the key we want if it has no value exit
    entry = data.get(name)
    if not entry:
        return None

    return Contact(
        name=name,
        address=entry.get("address", {}),
        billing_details=entry.get("billing_details", {}),
    )


class TestContactWithJSON(unittest.TestCase):
    def setUp(self):
        # Create a temporary JSON to simulate a database call.
        self.db_path = "test_contacts.json"
        self.sample_data = {
            "John Robbo": {
                "address": {"city": "Subiaco", "state": "WA", "postcode": "6022"},
                "billing_details": {"card_type": "Visa", "expiration_date": "12/27"}
            },
            "Dean Nguyen": {
                "address": {"city": "Joondalup", "state": "WA", "zip": "6043"},
                "billing_details": {"card_type": "Mastercard", "expiration_date": "11/26"}
            }
        }
        with open(self.db_path, "w", encoding="utf-8") as file:
            json.dump(self.sample_data, file, indent=2)

    def tearDown(self):
        # Clean up the temporary JSON file
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_get_contact_info_found(self):
        # Get this working
        result = get_contact_info("John Robbo", db_path=self.db_path)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "John")
        # self.assertEqual(result.address, {})
        # self.assertEqual(result.billing_details, {})

    def test_get_contact_info_not_found(self):
        result = get_contact_info("Guido Verschoor", db_path=self.db_path)
        self.assertIsNone(result)

    def test_get_contact_info_missing_file(self):
        # Ensure function returns None if DB  or DB file doesn't exist
        result = get_contact_info("John Robbo", db_path="does_not_exist.json")
        self.assertIsNone(result)

    def test_get_contact_info_malformed_json(self):
        # Write malformed data structure, expect None
        with open(self.db_path, "w", encoding="utf-8") as f:
            f.write('{"John Robbo": {"address": {"city": "Sydney"}}')
        result = get_contact_info("John Doe", db_path=self.db_path)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
