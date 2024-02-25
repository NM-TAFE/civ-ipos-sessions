# test_project.py

import unittest
from src.project import Project
from src.organisation import Organisation
from src.contact import Contact

class TestProject(unittest.TestCase):
    def test_project_creation(self):
        # Create an organization
        org = Organisation("NM Tafe")
        # Create a project associated with the organisation
        project = Project("Project Diploma", org)

        # # Check if project is associated with the correct organisation
        self.assertEqual(project.organisation.name, "NM Tafe")
        self.assertEqual(project.name, "Project Diploma")
        self.assertEqual(project.organisation, org)

    # Challenge - Add a test that tests a contact can be created and
    # added to an organisation and can also be added to a project

    # Challenge Solution - test that you can add a contact to an organisation
    # and a project using the project class
    def test_add_contact_to_project(self):
        org = Organisation("Company")
        contact = Contact("John Doe", "john@example.com")
        org.add_contact(contact)

        project = Project("Project X", org)
        project.add_contact(contact)

        self.assertIn(contact, project.contacts)


if __name__ == '__main__':
    unittest.main()
