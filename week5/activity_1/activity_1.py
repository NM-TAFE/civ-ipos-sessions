# Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal

# Main program logic

    # Open the binary file for reading and create output text and bytes files for writing using the context manager

        # Iterate through each line in the binary file

            # Decode the line to Unicode string and remove leading/trailing whitespaces


            # Check if the line starts with "TEXT:"

                # Extract text content, convert to uppercase, and write to text file


            # Check if the line starts with "BYTES:"
            # elif line.startswith("BYTES:"):

                # Extract the string and encode to hexadecimal

                # Extract byte content, convert to bytes object(using fromhex()), 
     
                # reverse bytes, and write to bytes file


    # Print success message


# Handle file I/O errors


# Handle other exceptions using the exception class

