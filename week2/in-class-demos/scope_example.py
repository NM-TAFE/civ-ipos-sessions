# Global variable
global_result = 0


def calculator(a, b, operation):
    # Local variable
    local_result = 0

    if operation == "add":
        local_result = a + b
    elif operation == "subtract":
        local_result = a - b
    elif operation == "multiply":
        local_result = a * b
    elif operation == "divide" and b != 0:
        local_result = a / b
    else:
        return "Invalid operation or division by zero"

    # Modify global variable
    global global_result
    global_result = local_result

    return local_result


# Function calls
print(calculator(5, 3, "add"))  # Output: 8
print(calculator(10, 2, "multiply"))  # Output: 20

# Accessing the global variable
print("Global Result:", global_result)