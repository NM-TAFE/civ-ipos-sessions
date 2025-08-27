# Creating a binary file example representing a 2x2 grid with RGB values for each point

# Define the grid size
width = 3
height = 3

# Define the RGB values for each point
rgb_values = [
    (255, 0, 0),   # Point (0, 0)
    (0, 255, 0),   # Point (0, 1)
    (0, 0, 255),   # Point (1, 0)
    (255, 255, 0)  # Point (1, 1)
]

# Create the binary file content
binary_content = bytearray()
binary_content.extend(width.to_bytes(1, 'big'))
binary_content.extend(height.to_bytes(1, 'big'))

for rgb in rgb_values:
    for value in rgb:
        binary_content.extend(value.to_bytes(1, 'big'))

# Save to a binary file
binary_file_path = './rgb_grid.bin' # Mac file path
with open(binary_file_path, "wb") as binary_file:
    binary_file.write(binary_content)
