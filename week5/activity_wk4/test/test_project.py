import unittest

from src.project import Project
from src.organisation import Organisation
from src.contact import Contact


class TestProject(unittest.TestCase):
    # arrange
    # Step 4
    def _test_project_create(self):
        # Create an organisation
        org = Organisation('NM Tafe')
        # act
        # Create a project associated with the organisation
        project = Project('Project IPOS', org)

        print(org)

        # assert
        self.assertEqual(project.name, 'Project IPOS')
        self.assertEqual(project.org.name, 'NM Tafe')
        self.assertEqual(project.org, org)

    # Step 5
    # Add a test that test a contact can be created and
    def test_add_contact_to_project(self):
        # arrange
        # Create an organisation & contact
        org = Organisation('NM Tafe')
        contact = Contact('John R', 'test@example.com')
        org.add_contact(contact)
        # act
        # Create a project associated with the organisation
        project = Project('Project IPOS', org)
        project.add_contact(contact)

        # added to an organisation and can also be added to a project
        self.assertIn(contact, project.contacts)
        # Challenge test that you can add a contact to an organisation
        # and a project using the project class


if __name__ == '__main__':
    unittest.main()
