def main():
    # Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal
    def reverse_bytes(bytes_data):
        return bytes_data[::-1]

    def convert_bytes_to_text(bytes_data):
        return bytes_data.decode('utf-8') 

    def convert_text_to_bytes(bytes_data):
        return bytes_data.encode('utf-8') 

    # Main program logic
    try:
    # Open the binary file for reading and create output text and bytes files for writing using the context manager
        with open("./activity_1/data.bin", "rb") as file, \
            open("./activity_1/converted_text.txt", "w") as text_output, \
            open("./activity_1/reversed_bytes.bin", "wb") as bytes_output:
            # Iterate through each line in the binary file
            for line in file:
                # Decode the line to Unicode string and remove leading/trailing whitespaces
                line = line.decode('utf-8').strip()

                # Check if the line starts with "TEXT:"
                if line.startswith("TEXT:"):
                    continue

                # Check if the line starts with "BYTES:"
                elif line.startswith("BYTES:"):
                    encoded_hex_data = line[6:].encode().hex()
                    # Extract the string and encode to hexadecimal
                    bytes_data = bytes.fromhex(encoded_hex_data)
                    # Extract byte content, convert to bytes object(using fromhex()), 
                    print()
                    # reverse bytes, and write to bytes file
                    reversed_bytes = reverse_bytes(bytes_data)
                    bytes_output.write(reversed_bytes)

        # Print success message
        print(reversed_bytes)

    # Handle file I/O errors
    except IOError:
        print('You have no file')

    # Handle other exceptions using the exception class

if __name__ == "__main__":
    main()