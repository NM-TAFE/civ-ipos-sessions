def main():
    try:
        # Phase 1: File Navigation
        print("Phase 1: File Navigation")
        print("=======================")
        with open("data.bin", "rb") as file:
            # Navigate to the 5th byte position
            file.seek(4)
            # Read and print the next 4 bytes from the current position
            print("Next 4 bytes form the position is 5: ", file.read(4).decode('utf-8'))

            # Move the file pointer to the beginning of the file
            file.seek(0)
            # Read and print the first 8 bytes from the file
            print("First 8 bytes form the file: ", file.read(8).decode('utf-8'))

            # Print the current file pointer position
            print(f"Current position is: {file.tell()}")

            # Use the find() method to search for the string "ABC" in the file
            file.seek(0)
            position = file.read().find(b"ABC")

            if position != -1:
                 print(f"Position of ABC is: {position}")
            else:
                 print("String 'ABC' has not been found")
        
        print("\nPhase 2: Bookmarking File Pointer")
        print("=================================")
        # Re-open the data.bin file in binary write-append mode
        with open("data.bin", "ab") as file:
            # Use the tell() method to get the current file pointer position and store it as a bookmark
            bookmark = file.tell()
            print(f"Current position(bookmark): {bookmark}") 

            # Write the string "XYZ" to the file
            file.write(b"XYZ")

            # Use the bookmarked pointer position to append the string "123" to the file
            file.seek(bookmark)
            file.write(b"123")

    # create three non naked exception handlers for: 
    # not finding the file, i/o error & all other exceptions
    except FileNotFoundError:
        print(f"File not found: {file}")
    
    except IOError:
        print("Unable to read or write to file")

    except Exception as error:
        print(f"An error occured {error}")

if __name__ == "__main__":
    main()
