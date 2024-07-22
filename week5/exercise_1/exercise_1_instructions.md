## Challenge Task:

    - Write a Python program to read the binary file named data.bin, 
    - convert its contents into text and bytes, and process each line accordingly. 
    - For lines that start with the prefix TEXT:
    - convert the rest of the line to text (UTF-8 -encoding), and 
    - for lines that start with the prefix BYTES:, convert the rest of the line to bytes.

### Analysis and Conversion: Based on the content of each line:

    - For lines starting with TEXT:,convert the text to uppercase and write it to a new text file named converted_text.txt.
    
    - For lines starting with BYTES:, reverse the bytes and write the modified bytes to a new binary file named reversed_bytes.bin.

### Pseudo Code to help you

1. Define helper functions for:
    - text-to-bytes conversion
    - bytes-to-text conversion
    - byte reversal

2. Main program logic:
    a. Try:
        i. Using the context manager, open the binary file for reading and create output text and bytes files for writing.
        ii. Iterate through each line in the binary file.
            - Decode the line to Unicode string and remove leading/trailing whitespaces.
            - Check if the line starts with "TEXT:".
                - Extract text content, convert to uppercase, and write to text file.
            - Check if the line starts with "BYTES:".
                - Extract byte content, convert to bytes object, reverse bytes, and write to bytes file.
        iii. Print success message.
    
    b. Except IOError:
        - Handle file I/O errors.
    
    c. Except other exceptions:
        - Handle other exceptions.
