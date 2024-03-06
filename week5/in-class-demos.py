# # Slide 8
# # Open the file in binary mode to read bytes
# with open("example.txt", "rb") as file:
#     # Read the contents of the file as bytes
#     bytes_data = file.read()

#     # Print the bytes object
#     print("Bytes object:", bytes_data)

#     # Iterate over each byte and print its integer value
#     print("Byte integers:")
#     for byte in bytes_data:
#         print(byte)

#     # Iterate over each byte and print its hexadecimal representation
#     print("Byte hexadecimal representations:")
#     for byte in bytes_data:
#         print(hex(byte))

# # # Slide 14
# # binary_representation = ' '.join([bin(ord(c))[2:].zfill(8) for c in "Everything is Binary"])
# # print(binary_representation)

# # # Simpler explanation of bytes
# binary_representations = []

# for c in "Everything is Binary":
#     # Step 1: Get the Unicode code point of the character
#     unicode_code_point = ord(c)
#     print(f"Unicode point: {unicode_code_point}")

#     # Step 2: Convert the Unicode code point to binary and remove the prefix '0b'
#     binary_representation = bin(unicode_code_point)[2:]
#     print(f"Binary: {binary_representation}")

#     # Step 3: Fill the binary string with leading zeros to ensure it's 8 characters long
#     padded_binary_representation = binary_representation.zfill(8)
#     print(f"Padded binary: {padded_binary_representation}")

#     # Append the padded binary representation to the list
#     binary_representations.append(padded_binary_representation)

# # Print the binary representations
# for binary_repr in binary_representations:
#     print(binary_repr)


# Slide 20
# Define a Unicode string
unicode_str = "Hello, world!"

# Encode the Unicode string using UTF-8 encoding
bytes_obj_utf8 = unicode_str.encode('utf-8')

# Decode the bytes object back to a Unicode string
decoded_str = bytes_obj_utf8.decode('utf-8')

print()

# # Convert integer 42 to a bytes object
# bytes_42 = (42).to_bytes(1, byteorder='big') # b'*'

# # Convert the bytes object back to an integer
# integer_from_bytes = int.from_bytes(bytes_42, byteorder='big') # 42

# print("Bytes representation of 42:", bytes_42)
# print("Integer from bytes:", integer_from_bytes)

