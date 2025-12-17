def main():
    pass
    # File Navigation
    with open('data_v2.bin', 'rb') as file:
        # Navigate to the 5th byte position
        
        # Read and print the next 4 bytes from the current position

        # Move the file pointer to the beginning of the file

        # Read and print the first 100 pixels from the file

        # Print the current file pointer position

        # Use the find() method to search for the string "ABC" in the file

        # Get the position of the first pixel jump 10 and get the next pixel

        # Print them out

        # Re-open the data.bin file in binary write-append mode

            # Use the tell() method to get the current file pointer position and store it as a bookmark

            # Write the string "XYZ" to the file

            # Use the bookmarked pointer position to append the string "123" to the file

    # create three non naked exception handlers for: 
    # not finding the file, i/o error & all other exceptions


if __name__ == "__main__":
    main()
