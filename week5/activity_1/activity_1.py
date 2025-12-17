def main():
    # TODO Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal


    # Main program logic
    # TODO Open the binary file for reading and create output text and bytes files for writing using the context manager
    try:
        
                # Iterate through each line in the binary file
                for line in file:
                    # TODO Decode the line to Unicode string and remove leading/trailing whitespaces

                    # Check if the line starts with "TEXT:"
                    if line.startswith("TEXT:"):
                        # Extract text content, convert to uppercase, and write to text file
                        text_to_print = line[5:].upper()
                        text_output.write(text_to_print + '\n')
                    
                    # Check if the line starts with "BYTES:"
                    elif line.startswith("BYTES:"):
                        pass

                        # TODO Extract the string and encode to hexadecimal
       
                        # TODO Extract byte content, convert to bytes object(using fromhex()), 
     
                        # Using your helper functions 
                        # TODO 1. reverse bytes, and write to bytes file

                        # TODO 2. convert back to text

                        # TODO 3. convert back to bytes

                        # Write the bytes data
                        bytes_output.write(bytes_data)
    # TODO use the in built IOError class                 
    except:
        pass
        # Handle file I/O errors
        # IOError - see definition, also Documentation: https://docs.python.org/3/library/io.html#
        # print(binary_error_message.strerror)

        # Handle other exceptions using the exception class
        
if __name__ == "__main__":
    main()