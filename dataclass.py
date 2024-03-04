from dataclasses import dataclass

@dataclass
class Coordinates:
    latitude: float
    longitude: float

# Example usage:
coordinates = Coordinates(latitude=37.7749, longitude=-122.4194)
print("Coordinates:", coordinates)
