classDiagram
    class Organisation {
        - name: str
        - contacts: list
        + Organisation(name: str)
        + add_contact(contact: Contact)
        + get_contacts(): list
    }

    class Contact {
        - name: str
        - email: str
        + Contact(name: str, email: str)
    }

    class Project {
        - name: str
        - organisation: Organisation
        - contacts: list
        + Project(name: str, organisation: Organisation)
        + add_contact(contact: Contact)
    }

    Organisation --> Contact : "has many"
    Organisation --> Project : "owns"
    Project --> Contact : "has many"
