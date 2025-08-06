

# Create a Graph Class:
# Implement a Graph class to represent the map.
# The Graph class should allow adding locations as vertices and connections between them as edges.
# Add Locations and Connections:
# Add a few locations with specific names and latitudes.
# Connect these locations to simulate a map.
# Display the Map:
# Print the connections between locations to visualise the map structure.

from dataclasses import dataclass
# Define a Location Data Class
# Include name and latitude/longitude attributes.
class Location:
    name: str
    # latitude: float
    # longitude: float

class Graph:
    def __init__(self):
        # Dictionary to store location names as keys and lists of connected locations as values
        pass

    def add_location(self, location):
        # Create an empty list for each location's connections
        # Each location is now a vertice in the graph object
        pass


    def add_connection(self, location1_name, location2_name):
        pass
        # Search the dicitonary keys for the two locations

            # Add the connection bidirectionally
            # If both keys are found connect them by adding each to the Locations list
            # Check if location 2 is in the vertice for location 1
      
                # If location 2 is not there add to the location 1 list
  
            # Check if location 2 is in the vertice for location 1

                # If location 2 is not there add to the location 1 list

        # else:
        #     print(f"One or both locations '{location1_name}' and '{location2_name}' do not exist in the graph.")


# Example usage:
def main():
    # Step 1: Create 3 Locations exzmple
    location1 = Location(name="LocationA", latitude=40.7128, longitude=30.7008)

    # Step 2: Create a Graph and Add Locations
    graph = Graph()

    # Step 3: Add Connections - example usage
    graph.add_connection("LocationA", "LocationB")


    # Step 4: Display the Graph (Map)
    print("Map representation:")
    # graph.display()

if __name__ == "__main__":
    main()
