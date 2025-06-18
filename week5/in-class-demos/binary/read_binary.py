# Define the path to the binary file
binary_file_path = './rgb_grid.bin'  # Update this path to your local path

# Open and read the binary file
with open(binary_file_path, 'rb') as file:
    # Read the entire content of the file
    binary_content = file.read()

# Print the binary content in a readable format
print("Binary content (hexadecimal):")
print(" ".join(f"{byte:02x}" for byte in binary_content))

# Parse the binary content 1920x780
width = binary_content[0]
height = binary_content[1]
print(f"\nWidth: {width}")
print(f"Height: {height}")

# TODO Extract and print RGB values



# print("\nRGB Values:")
# for i, rgb in enumerate(rgb_values):
#     print(f"Point {i}: {rgb}")
