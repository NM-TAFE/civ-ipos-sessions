# We sometimes want to use nested loops to create multidimensional structures
# Now using dictionaries to associate each product code
# with a tuple containing the product name and its price.

# Define a function that creates the product lookup dictionary

    # TODO: Initialise an empty dictionary to store the catalog

    # TODO: Iterate over the outer keys (e.g., rows or categories)

        # TODO: Iterate over the inner keys (e.g., individual product codes)

            # TODO: Retrieve the product code

            # TODO: Use the corresponding product data as the value
            
            # TODO: Add the code-data pair to the catalog

    # Return the completed catalog


# Define the product code grid as a dictionary of dictionaries
product_code_grid = {
    'row1': {
        'col1': 'P1001',
        'col2': 'P1002'
    },
    'row2': {
        'col1': 'P1003',
        'col2': 'P1004'
    }
}

# Define the product data grid (names and prices) as a matching structure
product_data_grid = {
    'row1': {
        'col1': ('Apple', 1.20),
        'col2': ('Banana', 0.50)
    },
    'row2': {
        'col1': ('Cherry', 0.75),
        'col2': ('Date', 1.50)
    }
}

# Call the function with the new dictionary-based inputs
product_catalog = build_product_catalog(product_code_grid, product_data_grid)

# Display the resulting product catalog
print(product_catalog)

# Expected Output:
# {
#     'P1001': ('Apple', 1.2),
#     'P1002': ('Banana', 0.5),
#     'P1003': ('Cherry', 0.75),
#     'P1004': ('Date', 1.5)
# }
