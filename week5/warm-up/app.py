from src.organisation import *
from src.contact import *
from src.project import *


def main():
    org = Organisation("NM Tafe")

    contact = Contact("John Robertson", "john@example.com")
    org.add_contact(contact)

    # project = Project("Project IPOS", org)
    # project.add_contact(contact)
    #
    # print(f"Organisation: {org.name}")
    # print(f"Contacts: {org.contacts[0].name}")
    # print(f"Project Name & Owner: {project.name} - {project.contacts[0].name}")


if __name__ == "__main__":
    main()
