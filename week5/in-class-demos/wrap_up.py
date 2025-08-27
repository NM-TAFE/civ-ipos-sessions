# # Converting the string ‘Hello’
# # Convert the string "Hello" into different binary representations
hello_str = "Hello"

# # 1. Display "Hello" as binary
# hello_binary = ' '.join(format(ord(char), '08b') for char in hello_str)
# print("Binary representation of 'Hello':", hello_binary)

# 2. Display "Hello" as hexadecimal
# hello_hex = ' '.join(format(ord(char), '02x') for char in hello_str)
# print("Hexadecimal representation of 'Hello':", hello_hex)

# 3. Display "Hello" as escape hex format (used in strings)
# hello_escape_hex = ''.join(f'Ox{format(ord(char), "02x")}' for char in hello_str)
# print("Escape hex representation of 'Hello':", hello_escape_hex)

# # 4. Convert "Hello" into a bytes object
# hello_bytes = bytes(hello_str, 'utf-8')
# print("Bytes object of 'Hello':", hello_bytes)

# # 5. Convert "Hello" into a bytearray object
# hello_bytearray = bytearray(hello_str, 'utf-8')
# print("Bytearray object of 'Hello':", hello_bytearray)

# # Understanding 0x48 and \x48
# # Understanding 0x48 (Hexadecimal Number)
# print(0x48)  # Output: 72 (decimal value of 0x48)

# # Understanding \x48 (Escape Hex Notation)
# print("\x48")  # Output: H (ASCII character for 0x48)

# # Converting the RGB Color (160, 32, 240)
# # Now, we do the same for the RGB color purple (160, 32, 240)
purple_rgb = (160, 32, 240)

# # 1. Display RGB components as binary
# purple_binary = tuple(format(value, '08b') for value in purple_rgb)
# print("Binary representation of RGB (160, 32, 240):", purple_binary)

# # 2. Display RGB components as hexadecimal
# purple_hex = tuple(format(value, '02x') for value in purple_rgb)
# print("Hexadecimal representation of RGB (160, 32, 240):", purple_hex)

# # 3. Display RGB as escape hex
# purple_escape_hex = ''.join(f'\\x{format(value, "02x")}' for value in purple_rgb)
# print("Escape hex representation of RGB (160, 32, 240):", purple_escape_hex)

# # 4. Convert RGB values into a bytes object
# purple_bytes = bytes(purple_rgb)
# print("Bytes object of RGB (160, 32, 240):", purple_bytes)

# # 5. Convert RGB values into a bytearray object
purple_bytearray = bytearray(purple_rgb)
print("Bytearray object of RGB (160, 32, 240):", purple_bytearray)


# # | Value       | Binary Representation | Hexadecimal Representation | Escape Hex |
# # |-------------|-----------------------|----------------------------|------------|
# # | ‘H’ (72)    | 01001000              | 0x48                      | \x48       |
# # | ‘e’ (101)   | 01100101              | 0x65                      | \x65       |
# # | ‘l’ (108)   | 01101100              | 0x6c                      | \x6c       |
# # | ‘l’ (108)   | 01101100              | 0x6c                      | \x6c       |
# # | ‘o’ (111)   | 01101111              | 0x6f                      | \x6f       |
# # | 160 (R)     | 10100000              | 0xa0                      | \xa0       |
# # | 32 (G)      | 00100000              | 0x20                      | \x20       |
# # | 240 (B)     | 11110000              | 0xf0                      | \xf0       |

# with open("rgb_grid.bin", "r+b") as file:
#     file.truncate(5)  # Truncate file to 5 bytes

# # 6. Efficiently Reading Large Binary Files in Chunks
# with open("rgb_grid.bin", "rb") as file:
#     while chunk := file.read(1024):  # Read 1KB at a time
#         # Do something process(chunk)
#         pass

# 7. File Pointer Operations (seek and tell)
with open("rgb_grid.bin", "rb") as file:
    print(file.tell())  # Outputs: 0 (start)
    file.seek(5)
    print(file.tell())  # Outputs: 5
    data = file.read(3).decode('utf-8')
    print(data)  # Outputs: b'Wor'

# import struct
#
# # Packing an integer into binary format
# binary_data = struct.pack("I", 12345)  # 'I' = unsigned int (4 bytes)
# print(binary_data.hex())  # Outputs: '39300000' (Little-endian representation)
#
# # Unpacking binary data
# unpacked_value = struct.unpack("I", binary_data)[0]
# print(unpacked_value)  # Outputs: 12345
