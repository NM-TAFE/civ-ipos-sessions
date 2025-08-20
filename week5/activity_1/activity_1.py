def main():
    # Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal
    def reverse_bytes(bytes_data):
        return bytes_data[::-1]

    def convert_bytes_to_text(bytes_data):
        return bytes_data.decode('utf-8')

    def convert_text_to_bytes(bytes_data):
        return bytes_data.encode('utf-8')

    # Main program logic
    # Open the binary file for reading and create output text and bytes files for writing using the context manager
    try:
        with open("dat.bin", "rb") as file, \
            open("converted_text.txt", "w") as text_output, \
            open("reversed_bytes.bin", "wb") as bytes_output:
                # Iterate through each line in the binary file
                for line in file:
                    # Decode the line to Unicode string and remove leading/trailing whitespaces
                    line = line.decode('utf-8').strip()

                    # Check if the line starts with "TEXT:"
                    if line.startswith("TEXT:"):
                        # Extract text content, convert to uppercase, and write to text file
                        text_to_print = line[5:].upper()
                        text_output.write(text_to_print + '\n')
                    
                    # Check if the line starts with "BYTES:"
                    elif line.startswith("BYTES:"):
                        # pass
                        # Extract the string and encode to hexadecimal
                        text_to_encode = line[6:].encode().hex()
                        # Extract byte content, convert to bytes object(using fromhex()), 
                        bytes_data = bytes.fromhex(text_to_encode)
                        # reverse bytes, and write to bytes file
                        reverse_byte_object = reverse_bytes(bytes_data)
                        print(reverse_byte_object)
                        converted_once = convert_bytes_to_text(reverse_byte_object)
                        converted_twice = convert_text_to_bytes(converted_once)
                        bytes_output.write(bytes_data)
    except IOError as binary_error_message:
        # Handle file I/O errors
        # IOError - see definition, also Documentation: https://docs.python.org/3/library/io.html#
        print(binary_error_message.strerror)

        # Handle other exceptions using the exception class
if __name__ == "__main__":
    main()