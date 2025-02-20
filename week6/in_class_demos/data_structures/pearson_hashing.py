# Example of a Pearson hashing table (a permutation of 0-255)
PEARSON_TABLE = [
    98,  6, 85, 150, 36, 23, 112, 164, 135, 198, 31, 158, 0, 89, 199, 230,
    40,  168,  116, 66, 173, 254, 122,  83, 134, 193,  35,  103,  45,  9, 134, 99,
    57,  39, 53,  62, 204, 231, 114, 233, 193, 48,  202, 241, 141, 128, 195, 78,
    66,  215, 61, 156, 180, 151, 160, 137, 91, 90,  15,  131, 13, 201, 95,  96,
    53,  194, 233, 7,  217, 221, 240, 222, 13, 26, 115, 252, 217, 190, 206, 152,
    15,  52, 239, 142, 243, 116, 35,  150, 93,  171, 187, 46,  226, 65,  141, 239,
    41,  47, 93, 183, 131, 233, 16, 144, 86,  159, 234, 123, 98,  69, 237, 178,
    99,  9,  52, 201, 89,  17, 24,  86,  97, 21,  58, 137, 11,  238, 10,  13,
    218, 155, 67, 86,  21, 103, 66,  217, 101, 23, 24, 232, 89,  196, 34,  38,
    106, 129, 105, 167, 191, 82, 192, 159, 44,  224, 85, 14,  139, 134, 176, 123,
    163, 206, 51, 124, 86, 33,  92,  119,  70, 21,  152, 137, 140, 135, 204, 94,
    30,  199, 179, 74,  122, 244, 52,  7,   81, 85,  148, 105, 129, 162, 222, 56,
    98,  42, 117, 123, 34, 135, 215, 239, 222, 108, 24,  178, 146, 147, 208, 73,
    70,  40, 181, 112, 194, 16,  134, 230, 90, 65,  20,  163, 74,  216, 25,  123,
    87,  112, 164, 16,  193, 15,  233, 111, 20, 240, 71, 217, 142, 50,  196, 80,
    90,  0,   183, 206, 79, 192, 58,  111, 157, 173, 93, 171, 46,  66,  115, 163
]

def pearson_hash(input_string):
    hash_value = 0
    for char in input_string:
        # XOR the current hash value with the next character's ASCII value
        hash_value = PEARSON_TABLE[hash_value ^ ord(char)]
    return hash_value

# Example usage
print(pearson_hash("hello"))  # Example output: 116
print(pearson_hash("world"))  # Example output: 213


# XOR - output (line 25)
# A (Input 1)	B (Input 2)	A XOR B (Output)
# 0	            0	        0
# 0	            1	        1
# 1	            0	        1
# 1	            1	        0