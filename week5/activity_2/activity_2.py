def main():
    pass
        # Phase 1: File Navigation
    with open('data_v2.bin', 'rb') as file:
        # Navigate to the 5th byte position
        file.seek(3)
        # Read and print the next 4 bytes from the current position
        print(f'First 3 bytes {file.read(3).decode('utf-8')}')

        # Move the file pointer to the beginning of the file
        file.seek(0)
        # Read and print the first 100 pixels from the file
        print(f'First 100 pixels {file.read(300).decode('utf-8')}')

        print(f"Current position is: {file.tell()}")
        position = file.read().find(b'D5 CE C7')
        move_on = file.seek(20)
        position_2 = file.read().find(b'D5 CE C7')
        print(position)
        print(position_2)

            # Print the current file pointer position


            # Use the find() method to search for the string "ABC" in the file





        # Re-open the data.bin file in binary write-append mode

            # Use the tell() method to get the current file pointer position and store it as a bookmark


            # Write the string "XYZ" to the file


            # Use the bookmarked pointer position to append the string "123" to the file

    # create three non naked exception handlers for: 
    # not finding the file, i/o error & all other exceptions


if __name__ == "__main__":
    main()
