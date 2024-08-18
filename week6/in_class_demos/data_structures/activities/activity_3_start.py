# Define a Location Data Class:
# Create a Python data class named Location with name and latitude attributes.
# Create a Graph Class:
# Implement a Graph class to represent the map.
# The Graph class should allow adding locations as vertices and connections between them as edges.
# Add Locations and Connections:
# Add a few locations with specific names and latitudes.
# Connect these locations to simulate a map.
# Display the Map:
# Print the connections between locations to visualize the map structure.
from dataclasses import dataclass

class Location:
    name: str
    latitude: float
    longitude: float

class Graph:
    def __init__(self):
        # Dictionary to store location names as keys and lists of connected locations as values
        self.vertices = {}  

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

    def display(self):
        # Loop through the Graph object and print the connections
        pass
            # connections = " -> ".join()
            # print(f"{location}: {connections}")

# Example usage:
def main():
    # Step 1: Create Locations
    location1 = Location(name="LocationA", latitude=40.7128, longitude=30.7008)
    location2 = Location(name="LocationB", latitude=34.0522, longitude=31.7128)
    location3 = Location(name="LocationC", latitude=51.5074, longitude=34.5728)
    location4 = Location(name="LocationD", latitude=48.8566, longitude=38.7333)

    # Step 2: Create a Graph and Add Locations
    graph = Graph()
    graph.add_location(location1)
    graph.add_location(location2)
    graph.add_location(location3)
    graph.add_location(location4)

    # Step 3: Add Connections
    graph.add_connection("LocationA", "LocationB")
    graph.add_connection("LocationA", "LocationC")
    graph.add_connection("LocationB", "LocationD")
    graph.add_connection("LocationC", "LocationD")

    # Step 4: Display the Graph (Map)
    print("Map representation:")
    graph.display()

if __name__ == "__main__":
    main()
