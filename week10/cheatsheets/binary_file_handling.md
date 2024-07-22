# Binary File Handling

## Basic Concepts

- **File Modes**: `rb` (read binary), `wb` (write binary), `ab` (append binary)
- **Methods**: `read()`, `write()`, `seek()`, `tell()`

| Topic                    | Description                                  | Syntax/Usage                                              |
|--------------------------|----------------------------------------------|-----------------------------------------------------------|
| File Opening             | Open a binary file                           | `f = open('file.bin', 'rb')`                              |
| File Closing             | Close a binary file                          | `f.close()`                                               |
| Read Binary Data         | Read data from a binary file                 | `data = f.read()`                                         |
| Read Fixed Bytes         | Read specific number of bytes                | `data = f.read(10)`                                       |
| Write Binary Data        | Write data to a binary file                  | `f.write(b'\x01\x02')`                                    |
| Append Binary Data       | Append data to existing binary file          | `f = open('file.bin', 'ab'); f.write(b'\x03')`            |
| Seek                     | Move to a specific position                  | `f.seek(5)`                                               |
| Tell                     | Get the current position                     | `pos = f.tell()`                                          |
| Read Structured Data     | Reading data into specific data structures   | `import struct; struct.unpack('I', f.read(4))`             |
| Write Structured Data    | Writing structured data                      | `import struct; f.write(struct.pack('I', 42))`            |

## Examples

### File Opening

```python
f = open('file.bin', 'rb')
```

### File Closing

```python
f.close()
```

### Read Binary Data

```python
data = f.read()
```

### Read Fixed Bytes

```python
first_ten_bytes = f.read(10)
```

### Write Binary Data

```python
f = open('file.bin', 'wb')
f.write(b'\x01\x02\x03')
```

### Append Binary Data

```python
f = open('file.bin', 'ab')
f.write(b'\x04')
f.close()
```

### Seek & Tell

```python
f.seek(5)
pos = f.tell()  # Should return 5
```
### Iterating over bytes
If you have read _bytes_, you can then iterate over the `bytes` object. Each item in a `bytes` object is an `int` with a value 0-255 (i.e. interprets each byte as an 8-bit unsigned int).
```python
first_ten_bytes = f.read(10)
for byte in first_ten_bytes:
    print(byte) # prints a number between 0-255
print(type(byte)) # returns int as the type
```

### Read Structured Data

```python
import struct
integer_data = struct.unpack('I', f.read(4))
```

### Write Structured Data

```python
import struct
f.write(struct.pack('I', 42))
```
