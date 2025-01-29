## Instructions for Students:

### Phase 1: File Navigation

- Open the data.bin file in binary read mode.
- Use the seek() method to navigate to the 5th byte position.
- Read and print the next 4 bytes from the current position.
- Move the file pointer to the beginning of the file.
- Read and print the first 8 bytes from the file.
- Print the current file pointer position.
- Use the find() method to search for the string "ABC" in the file. 
- Print the position if found, otherwise print a message indicating it was not found.


### Phase 2: Bookmarking File Pointer

- Re-open the data.bin file in binary write-append mode.
- Use the tell() method to get the current file pointer position and store it as a bookmark.
- Write the string "XYZ" to the file.
- Use the bookmarked pointer position to append the string "123" to the file.