# main.py 
# Organisation data 
organisations = [] 

# Contact data 
contacts = [] 
  
# Project data 
projects = [] 

# Function to add a contact to an organisation 
def add_contact(org_index, contact_index): 
    organisations[org_index]["contacts"].append(contact_index) 

# Function to add a project to an organisation 
def add_project(org_index, project_index): 
    organisations[org_index]["projects"].append(project_index) 

# Initialise organisations 
organisations.append({"name": "XYs Corp", "contacts": [], "projects": []}) 

# Initialise contacts 
contacts.append({"name": "John Doe", "email": "john@example.com", "phone": "0888888888"})

# Initialise projects 
projects.append({"name": "Project X", "description": "Description of Project X"}) 

# Add contact to organisation 
add_contact(0, 0) 

# Add project to organisation 
add_project(0, 0) 

# Display organisation details 
print("Organisation Name:", organisations[0]["name"]) 
print("Contacts:") 

for contact_index in organisations[0]["contacts"]: 
    print("\tName:", contacts[contact_index]["name"]) 
    print("\tEmail:", contacts[contact_index]["email"]) 
    print("\tPhone:", contacts[contact_index]["phone"]) 

print("Projects:") 

for project_index in organisations[0]["projects"]: 
    print("\tName:", projects[project_index]["name"]) 
    print("\tDescription:", projects[project_index]["description"]) 

 